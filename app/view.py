# coding: utf-8

from mako.template import Template

class View_cl(object):

	def __init__(self):
		pass

	def error(self, code="500"):
		template = Template(filename="content/error.html")
		return template.render(code=code)

# EOF