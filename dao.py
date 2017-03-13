#!/usr/local/bin/python3

import os, sqlite3, time, datetime, re

class DBObject:
    FIELD_CONV = {
        'objectId': 'id',
        'c_id': 'id',
        'id': 'id',
        'created_at': 'c_createdAt',
    }

    OPER_CONV = {
        'gt': '>',
        'lt': '<',
        'gte': '>=',
        'lte': '<=',
        'ne': '!=',
        'contains': 'like'
    }

    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self, **kwargs):
        import hashlib
        self.dict = {}
        self.conn = sqlite3.connect('my.db')
        self.table_name = self.__class__.__name__
        self.dict['id'] = hashlib.md5(('%.6f' % time.time()).encode('utf-8')).hexdigest()
        self.dict['createdAt'] = datetime.datetime.now().strftime(DBObject.DATETIME_FORMAT)
        for col, default in self.__class__.__dict__.items():
            if col.startswith('__'): continue
            self.dict[col] = default
        for _ in kwargs:
            if _ in self.dict:
                self.dict[_] = kwargs[_]

    def set(self, key, value):
        self.dict[key.lower()] = value

    def get(self, key, default=''):
        return self.dict.get(key.lower(), default)

    @property
    def id(self):
        return self.dict.get('id')

    @property
    def created_at(self):
        return self.dict['createdAt']

    def get_cols(self):
        c = self.conn.cursor()
        cols = c.execute("select * from sqlite_master where type = 'table' and name= '" + self.table_name + "'").fetchone()[-1].lower()

        cols = cols[cols.find('(')+1:cols.rfind(')')].replace('`', '')
        cols = re.split(r',\s*', cols)
        cols = [re.split(r'\s', _)[0] for _ in cols]
        cols = [_ if _ == 'id' else _[2:] for _ in cols]

        return cols

    def select(self, order='', **kwargs):
        c = self.conn.cursor()
        where = ''
        for k in kwargs:
            field = k.split('__')[0]
            oper = '=' if '__' not in k else DBObject.OPER_CONV.get(k.split('__')[1], '=')
            if oper == 'like': kwargs[k] = '%' + kwargs[k] + '%'
            where += '`' + DBObject.FIELD_CONV.get(field, 'c_' + field) + '` ' + oper + ' ?'


        if where != '':
            where = ' WHERE ' + where
        where_args = list(kwargs.values())

        if order != '':
            order = ' ORDER BY ' + ','.join([DBObject.FIELD_CONV.get(_, 'c_' + _) + (' desc' if _.startswith('-') else '') for _ in order.split(',')]).replace('-', '')

        where += order
        
        cols = self.get_cols()

        r = []
        for res in c.execute("SELECT * FROM " + self.table_name + where, where_args):
            k = self.__class__()
            for i in range(0, len(res)):
                try:
                    x = json.loads(res[i])
                except:
                    x = res[i]
                k.set(cols[i], x)
            r.append(k)
        return r

    def save(self):
        if 'objectId' in self.dict:
            self.dict['id'] = self.dict['objectId']
            del self.dict['objectId']

        create = "CREATE TABLE IF NOT EXISTS " + self.table_name + " (id TEXT PRIMARY KEY"
        for c in self.dict.keys():
            if c.lower() == 'id': continue
            create += ", `c_" + c + "` " + ("INTEGER" if isinstance(self.dict[c], int) else "REAL" if isinstance(self.dict[c], float)  else "TEXT")
        create += ")"
        c = self.conn.cursor()
        c.execute(create)

        cols = self.get_cols()
        for _ in list(self.dict.keys()):
            if _.lower() not in cols: del self.dict[_]
        colcount = len(self.dict)

        sql = "REPLACE INTO " + self.table_name + "(" + ','.join([('' if _ == 'id' else 'c_') + _ for _ in self.dict.keys()]) + ") VALUES (" + ("?," * colcount)[:-1] +  ")"
        vals = tuple(json.dumps(_) if isinstance(_, type([])) or isinstance(_, type({})) else _ for _ in self.dict.values())
        c.execute(sql, vals)
        self.conn.commit()
        return self

class File:
    BASE = 'static/files'

    def __init__(self, token, stream):
        import hashlib
        self.id = hashlib.md5(('%.6f' % time.time()).encode('utf-8')).hexdigest()
        self.url = '/' + File.BASE + '/' + self.id + '.' + token[token.rfind('.')+1:]
        self.stream = stream

    def save(self):
        if not os.path.exists(File.BASE):
            os.mkdir(File.BASE)
        with open(self.url[1:], 'w') as f:
            f.write(self.stream.read())

