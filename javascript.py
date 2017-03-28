#!/usr/bin/env python3
import ast

import sys

class NotSupportedInJS(Exception):
    pass
    
class ExpParser(ast.NodeVisitor):
    for_count = 0
    context = [None]
    buf = ''
    
    identifiers = {}
    
    def print_(self, *args):
        s = ' '.join([str(_) for _ in args])
        for _ in self.context:
            if hasattr(_, 'refrain') and _.refrain:
                self.buf += s
                return
        self.buf = ''
        sys.stdout.write(s)
        
    def print(self, *args):
        self.print_(*args)
        self.print_('\n')
    
    def print_indent(self):
        self.print_('  ' * (len(self.context) - 3))
        
    def print_notsupported(self):
        self.print_('/* Not Supported */')
        
    def register_id(self, node, typ):
        def _id(n):
            if hasattr(n, 'id'): return n.id
            elif hasattr(n, 'name'): return n.name
            else: return ''
        
        gid = _id(node)
        while hasattr(node, 'parent') and node.parent:
            gid = _id(node.parent) + '.' + gid
            node = node.parent
            
        self.identifiers[gid] = typ
        
    ###
    
    def visit(self, node):
        if not node:
            self.print_('null')
            return
            
        node.parent = None
        t = list(self.context)
        t.reverse()
        for _ in t:
            if type(_) in [ast.ClassDef, ast.FunctionDef]:
                node.parent = _
                break
                
        self.context.append(node)
        super().visit(node)
        self.context.pop()

    def generic_visit(self, node):
        self.print('/* Not Supported: ' + type(node).__name__ + ' */')
        for field, value in reversed(list(ast.iter_fields(node))):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)
                    elif isinstance(value, ast.AST):
                        self.visit(value)

    # literals
    
    def visit_Num(self, node):
        self.print_(node.n)
        
    def visit_Str(self, node):
        self.print_('"%s"' % node.s)
        
    def visit_Bytes(self, node):
        self.print_(node.s)
        
    def visit_List(self, node):
        self.print_('[')
        first = True
        
        for n in node.elts:
            if not first:
                self.print_(', ')
                
            self.visit(n)
            first = False
            
        self.print_(']')

    def visit_Dict(self, node):
        self.print('{')
        first = True
        for k, v in zip(node.keys, node.values):
            if not first:
                self.print(',')
                
            if not hasattr(k, 's'):
                self.print_notsupported()
            self.print_('"%s": ' % (k.s,))
            self.visit(v)
            first = False
        
        self.print('')
        self.print_('}')
        
    def visit_NameConstant(self, node):
        if node.value is True:
            self.print_('true')
        elif node.value is False:
            self.print_('false')
        elif node.value is None:
            self.print_('null')

    # operators
    
    def get_op(self, oper):
        t_op = type(oper)
        if t_op is ast.Add       : op = '+'
        elif t_op is ast.Sub     : op = '-'
        elif t_op is ast.Mult    : op = '*'
        elif t_op is ast.Div     : op = '/'
        elif t_op is ast.FloorDiv: op = 'floordiv'
        elif t_op is ast.Mod     : op = '%'
        elif t_op is ast.Pow     : op = '**'
        elif t_op is ast.LShift  : op = '<<'
        elif t_op is ast.RShift  : op = '>>'
        elif t_op is ast.BitOr   : op = '|'
        elif t_op is ast.BitXor  : op = '^'
        elif t_op is ast.BitAnd  : op = '&'
        
        elif t_op is ast.And: op = '&&'
        elif t_op is ast.Or: op = '||'
        elif t_op is ast.Eq     : op = '=='
        elif t_op is ast.NotEq: op = '!='
        elif t_op is ast.Lt   : op = '<'
        elif t_op is ast.LtE  : op = '<='
        elif t_op is ast.Gt   : op = '>'
        elif t_op is ast.GtE  : op = '>='
        elif t_op is ast.Is   : op = '==='
        elif t_op is ast.IsNot: op = '!=='
        elif t_op is ast.In   : op = 'in'
        elif t_op is ast.NotIn: op = 'notin'
        
        elif t_op is ast.UAdd : op = '+'
        elif t_op is ast.USub : op = '-'
        elif t_op is ast.Not  : op = '!'
        elif t_op is ast.Invert: op = '~'
        return op
            
    # variables
    
    def visit_Name(self, node):
        self.print_(node.id)
        
    def visit_UnaryOp(self, node):
        op = self.get_op(node.op)
        self.print_(op)

        self.print_('(')
        self.visit(node.operand)
        self.print_(')')
    
    def visit_BinOp(self, node):
        op = self.get_op(node.op)
        if op == 'floordiv':
            self.print_('Math.floor((')
            self.visit(node.left)
            self.print_(')/(')
            self.visit(node.right)
            self.print_('))')
        else:
            self.print_('(')
            self.visit(node.left)
            self.print_(')')
            self.print_(op)
            self.print_('(')
            self.visit(node.right)
            self.print_(')')
            
    def visit_BoolOp(self, node):
        op = self.get_op(node.op)
        self.print_('(')
        self.visit(node.left)
        self.print_(')')
        self.print_(op)
        self.print_('(')
        self.visit(node.right)
        self.print_(')')
        
    def visit_Compare(self, node):
        if len(node.comparators) > 1:
            self.print_notsupported()
        
        op = self.get_op(node.ops[0])
        if op not in ['in', 'notin']:        
            self.print_('(')
            self.visit(node.left)
            self.print_(')')
            self.print_(op)
            self.print_('(') 
            self.visit(node.comparators[0])
            self.print_(')')
        else:
            # self.print_('(') 
            # self.visit(node.comparators[0])
            # self.print_(').indexOf(')
            # self.visit(node.left)
            # self.print_(') >= 0 || (')
            # self.visit(node.comparators[0])
            # self.print_(')[')
            # self.visit(node.left)
            # self.print_('] === undefined')
            self.print_notsupported()
            
    def visit_Call(self, node):
        
        self.buf = ''
        node.refrain = True
        self.visit(node.func)
        node.refrain = False
        
        if self.identifiers.get(self.buf, 'func') == 'class':
            self.print_('new ' + self.buf)
        
        self.print_(self.buf)
            
        self.print_('(')
        first = True
        
        for _ in node.args:
            if not first:
                self.print_(', ')
            self.visit(_)
            first = False
            
            
        self.print_(')')
    
    def visit_Attribute(self, node):
        self.visit(node.value)
        self.print_('.')
        self.print_(node.attr)
        
    def visit_IfExp(self, node):
        self.print_('(')
        self.visit(node.test)
        self.print_(') ? (')
        for _ in node.body if isinstance(node.body, list) else [node.body]:
            self.visit(_)
        self.print_(') : (')
        for _ in node.orelse if isinstance(node.orelse, list) else [node.orelse]:
            self.visit(_)
        self.print_(')')
        
    # subscripting
    
    def visit_Subscript(self, node):
        self.visit(node.value)
        if type(node.slice) is not ast.Index:
            self.print_notsupported()
        self.print_('[')
        self.visit(node.slice)
        self.print_(']')
        
    def visit_Index(self, node):
        self.visit(node.value)
    
    # Comprehensions are not supported in JS
    
    # Statements
    
    def visit_Assign(self, node):
        self.print_indent()
        
        self.register_id(node.targets[0], 'var')
            
        if len(node.targets) == 1:
            self.visit(node.targets[0])
            self.print_(' = ') 
            self.visit(node.value)
            self.print(';')
                
    def visit_AugAssign(self, node):
        self.print_indent()
        op = self.get_op(node.op)
        self.visit(node.target)
        
        self.register_id(node.target, 'var')
        
        if op in '+-' and type(node.value) is ast.Num and node.value.n == 1:
            self.print_(op * 2)
        else:
            self.print_('', op + '=', ' ')
            self.visit(node.value)
        self.print(';')
                
    def visit_Pass(self, node):
        self.print_indent()
        self.print(';')
            
    def visit_If(self, node):
        self.print_indent()
        self.print_('if (')
        self.visit(node.test)
        self.print(') {')
        for _ in node.body:
            self.visit(_)
        self.print_indent()
        self.print_('}')
        
        if node.orelse:
            self.print('else {')
            for _ in node.orelse:
                self.visit(_)
            self.print_indent()
            self.print_('}')
        self.print()
        
    def visit_Expr(self, node):
        self.print_indent()
        self.visit(node.value)
        self.print(';')
        
    def visit_Module(self, node):
        for _ in node.body:
            self.visit(_)
            
    def visit_For(self, node):
        self.print_indent()
        self.for_count += 1
        self.print_('var for_range%d = ' % self.for_count)
        self.visit(node.iter)
        self.print(';')
        self.print_indent()
        self.print('for (var for_iter# = 0; for_iter# < for_range#.length; ++for_iter#) {'.replace('#', str(self.for_count)))
        self.print_indent()
        self.print_('  var ')
        self.visit(node.target)
        self.print(' = for_range#[for_iter#];'.replace('#', str(self.for_count)))
        for _ in node.body:
            self.visit(_)
        self.print_indent()
        self.print('}')
        
    def visit_While(self, node):
        self.print_indent()
        self.print_('while (')
        self.visit(self.test)
        self.print(') {')
        for _ in node.body:
            self.visit(_)
        self.print('}')
        
    def visit_Break(self, node):
        self.print_indent()
        self.print('break;')
        
    def visit_Continue(self, node):
        self.print_indent()
        self.print('break;')
        
    def visit_Try(self, node):
        self.print_indent()
        self.print('try {')
        for _ in node.body: self.visit(_)
        self.print_indent()
        self.print('} catch (python_err) {')
        self.context.append('catch')
        for _ in node.handlers:
            self.print_indent()
            self.print_('if (python_err.__not_real__inherits("')
            self.visit(_.type)
            self.print('")) {')
            self.context.append('_js_if_')
            self.print_indent()
            self.print('  var %s = python_err;' % (_.name))
            for __ in _.body: self.visit(__)
            self.context.pop()
            self.print_indent()
            self.print('}')
        self.context.pop()
        self.print_indent()
        self.print('}')
        
    # Function and Class
        
    def visit_Lambda(self, node):
        self.print_('function (' + ', '.join([_.arg for _ in node.args.args]) + ') { return ');
        self.visit(node.body)
        self.print_('; }')
        
    def visit_FunctionDef(self, node):
        self.print_indent()
        
        self.register_id(node, 'func')
        
        global_ids = dict(self.identifiers)
        
        inclass = isinstance(node.parent, ast.ClassDef)
        fmt = 'funciton %s(%s) {' if not inclass else 'this.%s = function (%s) {'
        args = node.args.args
        
        if inclass: 
            self_arg = node.args.args[0].arg
            if not hasattr(node.parent, 'members'):
                node.parent.members = {}
            node.parent.members[node.name] = args
            first_arg = args[0].arg
            args = args[1:]
        
        args = [_.arg for _ in args]
        self.print(fmt % (node.name, ', '.join(args)))
        
        if inclass:
            self.print_indent()
            self.print('  var %s = this;' % first_arg)
        
        node.refrain = True
        for _ in node.body: self.visit(_)
        
        defined = []
        for _ in self.identifiers:
            if self.identifiers[_] == 'var' and _ not in global_ids and _ not in args and _ != first_arg:
                defined.append(_)
        
        node.refrain = False
        if len(defined) > 0:
            self.print_indent()
            self.print('  var', ', '.join([_.split('.')[-1] for _ in defined]) + ';')
        
        for _ in node.body: self.visit(_)
        
        self.print_indent()
        self.print('}')
        
        self.identifiers = global_ids
        
    def visit_Return(self, node):
        self.print_indent()
        self.print_('return ')
        self.visit(node.value)
        self.print(';')
        
    def visit_ClassDef(self, node):
        self.print_indent()
        
        self.register_id(node, 'class')
        
        node.refrain = True
        for _ in node.body:
            self.visit(_)
        node.refrain = False
        
        init_args = []
        if hasattr(node, 'members') and '__init__' in node.members:
            init_args = node.members['__init__']

        fmt = 'function %s(%s) {'
        if isinstance(node.parent, ast.ClassDef):
            fmt = 'this.%s = function (%s) {'

        self.print(fmt % (node.name, ', '.join([_.arg for _ in init_args[1:]])))
        
        for _ in node.body:
            self.visit(_)
                
        if hasattr(node, 'members') and '__init__' in node.members:
            self.print_indent()
            self.print('  this.__init__(%s);' % ', '.join([_.arg for _ in init_args[1:]]))
        
        self.print_indent()
        self.print('}')
        
if __name__ == '__main__':
    py = open(sys.argv[1]).read()
    node = ast.parse(py)
    v = ExpParser()
    v.visit(node)
