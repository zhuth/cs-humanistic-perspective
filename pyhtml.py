#!/usr/local/bin/python3

import json, re

class HTMLTag:
	def __init__(self, *args, **kwargs):
		self.tag = self.__class__.__name__.lower().split('_')[-1]
		self.endprefix = '/'
		self._deal_with_args(args, kwargs)
		self.indent = 0

	def _deal_with_args(self, args, kwargs):
		self.attr = kwargs
		if len(kwargs) == 0 and len(args) == 1 and isinstance(args[0], dict):
			self.children = []
			self.attr = args[0]
		else:
			self.children = []
			for arg in args:
				if isinstance(arg, list): self.children += arg
				else: self.children.append(arg)

	def __str__(self):
		CONV = {
			'_class': 'class',
			'Class': 'class'
		}

		from xml.sax.saxutils import escape, unescape
		# escape() and unescape() takes care of &, < and >.
		html_escape_table = {
		'"': "&quot;",
		"'": "&apos;",
		"\n": "<br />",
		}

		def html_escape(text):
			return escape(text, html_escape_table)


		attrs = ''
		for k in self.attr:
			if isinstance(self.attr[k], list):
				self.attr[k] = ' '.join([str(_) for _ in self.attr[k]])
			attrs += ' ' + CONV.get(k, k) + '="' + str(self.attr[k]) + '"'

		idt = ' ' * self.indent
			
		h = idt + '<' + self.tag + attrs
		if len(self.children) == 0:
			h+= ' />'
		else:
			h += '>'

			pureText = True
			for _ in self.children:
				if isinstance(_, HTMLTag): pureText = False

			if pureText:
				h += html_escape(''.join(self.children)) + '<' + self.endprefix + self.tag + '>'
			else:
				h += '\n'
				for _ in self.children:
					if isinstance(_, HTMLTag):
						_.indent = self.indent + 4
					h += (' ' * (self.indent + 4) + html_escape(_) if isinstance(_, str) else str(_)) + '\n'
				h += idt + '<' + self.endprefix + self.tag + '>'

		return  h

	def __getitem__(self, index):
		if isinstance(index, int):
			return self.children[index]
		else:
			if not isinstance(index, HTMLTag):
				t = HTMLTag()
				t.tag = str(index)
				index = t
			if index.tag == self.attr.get('id'):
				return self
			res = []
			for _ in self.children:
				if not isinstance(_, HTMLTag): continue
				cres = _[index] 
				if isinstance(cres, list): res += cres
				else: res += [cres]

				if index.tag != '' and _.tag != index.tag: continue
				flag = True
				for att, atv in index.attr.items():
					if att not in _.attr:
						flag = False
						continue
					if isinstance(atv, list) and set(atv) <= set(_.attr[att]):
						pass
					elif isinstance(_.attr[att], list) and set([atv]) <= set(_.attr[att]):
						pass
					elif atv == _.attr[att]:
						pass
					else:
						flag = False
						break
				if not flag: continue
				res.append(_)
			return res[0] if len(res) == 1 else res


	def append(self, ele):
		self.children.append(ele)
		return self

	def remove(self, ele):
		self.children.remove(ele)
		return self

	def removeAt(self, index):
		del self.children[index]

	def insert(self, index, ele):
		self.children.insert(index, ele)

class A(HTMLTag):
	pass

class DIV(HTMLTag):
	pass

class P(HTMLTag):
	pass

class H1(HTMLTag):
	pass

class H2(HTMLTag):
	pass

class H3(HTMLTag):
	pass

class H4(HTMLTag):
	pass

class H5(HTMLTag):
	pass

class BLOCKQUOTE(HTMLTag):
	pass

class B(HTMLTag):
	pass

class I(HTMLTag):
	pass

class S(HTMLTag):
	pass

class HEAD(HTMLTag):
	pass

class BODY(HTMLTag):
	pass

class HEAD(HTMLTag):
	pass

class TITLE(HTMLTag):
	pass

class META(HTMLTag):
	pass

class HTML(HTMLTag):
	pass

class SPAN(HTMLTag):
	pass

class TABLE(HTMLTag):
	pass

class THEAD(HTMLTag):
	pass

class TBODY(HTMLTag):
	pass

class TR(HTMLTag):
	pass

class TD(HTMLTag):
	pass

class DD(HTMLTag):
	pass

class DT(HTMLTag):
	pass

class COMMENT(HTMLTag):
	def __init__(self, *args, **kwargs):
		self._deal_with_args(args, kwargs)
		self.tag = '!--'
		self.endprefix = '--'

	def __str__(self):
		return '<!-- ' + ''.join([str(_) for _ in self.children]) + ' -->'

class SCRIPT(HTMLTag):
	pass

class LINK(HTMLTag):
	pass

class IMG(HTMLTag):
	pass

class EM(HTMLTag):
	pass

class ANY(HTMLTag):
	def __init__(self, *args, **kwargs):
		self.tag = ''
		self._deal_with_args(args, kwargs)
		self.indent = 0
