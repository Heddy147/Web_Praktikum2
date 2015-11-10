# coding: utf-8
import cherrypy
from mako.template import Template

class Login_cl(object):

	def __init__(self):
		pass

	@cherrypy.expose
	def index(self, **kwargs):
		error = False
		if "username" in kwargs and "password" in kwargs:
			users = cherrypy.Application.db.load_user()
			if kwargs["username"] in users and users[kwargs["username"]]['password'] == kwargs['password']:
				cherrypy.Application.user.login_user(kwargs["username"], users[kwargs["username"]])
				raise cherrypy.HTTPRedirect("/themen/index")
			else:
				error = True

		template = Template(filename="content/login/index.html")
		return template.render(data=kwargs, error=error)

	@cherrypy.expose
	def logout(self):
		cherrypy.Application.user.logout()
		raise cherrypy.HTTPRedirect("/themen/index")

# EOF