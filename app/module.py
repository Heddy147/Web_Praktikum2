# coding: utf-8
import cherrypy


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
		print("no")
		return "no"

# EOF
