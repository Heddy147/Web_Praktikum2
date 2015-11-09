# coding: utf-8
import cherrypy

user = "admin"


class Application_cl(object):
	def __init__(self):
		pass

	@cherrypy.expose
	def default(self, *arglist, **kwargs):
		raise cherrypy.HTTPRedirect("/themen/index")

# EOF
