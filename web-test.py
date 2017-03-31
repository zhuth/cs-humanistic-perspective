#!/usr/local/bin/python3

#coding: utf-8
from flask import Flask
from flask import request, url_for, render_template, jsonify, Response
from pyhtml import *

import requests

app = Flask(__name__)

from dao import DBObject

class Book(DBObject):
    title = ''
    author = ''
    publisher = ''
    year = 2000
    isbn = ''
    doubanid = ''
    doubanpic = ''
    
class Annotation(DBObject):
    book = ''
    page = 0
    chapter = ''
    content = ''
    tag = ' '

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image_proc/<path:p>')
def image_proc(p):
    import requests
    from PIL import Image, ImageOps
    from io import BytesIO

    if not p.startswith('http://') and not p.startswith('https://'): p = 'http://' + p
    r = requests.get(p)
    if r.status_code == 200:
        img = Image.open(BytesIO(r.content))
        buf = BytesIO()
        ImageOps.autocontrast(img, 10).save(buf, 'jpeg')
        return Response(buf.getvalue(), mimetype="image/jpeg")

    return ''
    
@app.route('/books')
def books():
    books=[{
        'style_num': (i % 6) + 1,
        'link': url_for('list_annotations', book_id=_.id),
        'pic': _.get('doubanpic'),
        'title': _.get('title'),
        'author': _.get('author'),
        'publisher': _.get('publisher'),
        'year': _.get('year')
    } for i, _ in enumerate(Book().select())]
    return jsonify({'books': books})
    
@app.route('/add-book', methods=['GET'])
def add_book_form():
    return str(
        HTML(
            HEAD(TITLE("添加一本书")),
            BODY(
                FORM(action='', enctype='multipart/form-data', method='POST').append(
                    TABLE(
                        [TR(TD(tip), TD(INPUT(type='text', name=name))) for tip, name in zip(['标题', '作者', '年份', '出版社', 'ISBN'], ['title', 'author', 'year', 'publisher', 'isbn'])]
                    ),
                    INPUT(type='submit', value='提交')
                )
            )
        )
    )
    
@app.route('/add-book', methods=['POST'])
def add_book_deal():
    b = Book()
    for _ in request.form:
        b.set(_, request.form[_])
    
    isbn = b.get('isbn')
    r = requests.get('https://api.douban.com/v2/book/isbn/' + isbn)
    if r.status_code == 200: # 成功
        db = r.json()
        b.set('doubanid', db['id'])
        b.set('doubanpic', db['images']['medium'])

    b.save()
    return '添加成功！'
    
@app.route('/add-annotation/<book_id>', methods=['GET'])
def add_annotation_form(book_id):
    b = Book().select(id=book_id)[0]
    return str(
        HTML(
            HEAD(TITLE("添加读书笔记")),
            BODY(
                H1(b.get('title')),
                FORM(action='', enctype='multipart/form-data', method='POST').append(
                    TABLE(
                        TR(TD('页码'), TD(INPUT(type='text', name='page'))),
                        TR(TD('章节'), TD(INPUT(type='text', name='chapter'))),
                        TR(TD('内容'), TD(TEXTAREA(name='content', cols="40", rows="20"))),
                        TR(TD('标签'), TD(INPUT(type='text', name='tag'))),
                    ),
                    INPUT(type='hidden', name='book', value=book_id),
                    INPUT(type='submit', value='提交')
                )
            )
        )
    )
    
@app.route('/add-annotation/<book_id>', methods=['POST'])
def add_annotation_deal(book_id):
    a = Annotation()
    for _ in request.form:
        a.set(_, request.form[_])
    a.save()
    return '添加成功！'
    
@app.route('/annotations/<book_id>')
def list_annotations(book_id):
    b = Book().select(id=book_id)[0]
    anns = Annotation().select(book=book_id)
    return str(
        HTML(
            HEAD(TITLE("读书笔记")),
            BODY(
                H1(b.get('title') + ' 的相关笔记'),
                HR(),
                A('添加笔记', href=url_for('add_annotation_form', book_id=book_id)),
                UL([
                    LI(
                        '页码 %d' % _.get('page'), 
                        '章节' + _.get('chapter') + '\n',
                        _.get('content') + '\n',
                        '标签' + _.get('tag'),
                        A('删除', href=url_for('delete_annotation', annotation_id=_.id))
                    ) for _ in anns
                ])
            )
        )
    )
    
@app.route('/annotations/delete/<annotation_id>')
def delete_annotation(annotation_id):
    a = Annotation().select(id=annotation_id)[0]
    a.delete()
    return '删除成功！'
    
if __name__ == '__main__':
    app.debug = True
    app.run()