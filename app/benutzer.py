# coding: utf-8
import cherrypy
from mako.template import Template

class Benutzer_cl(object):

	def __init__(self):
		pass

	@cherrypy.expose
	def index(self):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")
		users = cherrypy.Application.db.load_user()

		template = Template(filename="content/benutzer/index.html")
		return template.render(users=users)

	@cherrypy.expose
	def create(self, **kwargs):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")
		error = False
		diskussionen = cherrypy.Application.db.load_diskussionen()

		if "diskussionen" not in kwargs:
			kwargs["diskussionen"] = []

		if "username" in kwargs and "password" in kwargs and "rolle" in kwargs:
			if cherrypy.Application.db.create_user(kwargs["username"], kwargs["password"], kwargs["rolle"], kwargs["diskussionen"]):
				raise cherrypy.HTTPRedirect("/benutzer")
			else:
				error = True

		template = Template(filename="content/benutzer/create.html")
		return template.render(diskussionen=diskussionen, error=error)

	@cherrypy.expose
	def delete(self, username):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")

		cherrypy.Application.db.delete_user(username)
		raise cherrypy.HTTPRedirect("/benutzer")

# EOF
