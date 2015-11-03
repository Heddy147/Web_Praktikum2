# coding: utf-8
import cherrypy
from mako.template import Template


class Module_cl(object):

	@cherrypy.expose
	def __init__(self):
		pass

	@cherrypy.expose
	def default(self, *arglist, **kwargs):
		print("jo")
		print(kwargs['al'])
		return "jo"

	@cherrypy.expose
	def test(self, *arglist, **kwargs):
		print(arglist)
		print(kwargs)

		mytemplate = Template(filename="content/module/test.html")
		return mytemplate.render(placeholder="Ihr Name123")

# EOF
