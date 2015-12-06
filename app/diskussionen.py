# coding: utf-8

import cherrypy
from mako.template import Template
from app import database


class Diskussionen_cl(object):

	db = None

	@cherrypy.expose
	def __init__(self):
		pass

	@cherrypy.expose
	def index(self, themen_id):
		cherrypy.Application.user.user_logged_in()
		diskussionen = cherrypy.Application.db.load_diskussionen(themen_id)

		template = Template(filename="content/diskussionen/index.html")
		return template.render(diskussionen=diskussionen, themen_id=themen_id)

	@cherrypy.expose
	def create(self, themen_id, **kwargs):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")
		print kwargs
		if "name" in kwargs and "beschreibung" in kwargs:

			cherrypy.Application.db.create_diskussion(themen_id, kwargs["name"], kwargs["beschreibung"])
			raise cherrypy.HTTPRedirect("/diskussionen/index/" + themen_id)

		template = Template(filename="content/diskussionen/create.html")
		return template.render(themen_id=themen_id)

	@cherrypy.expose
	def delete(self, themen_id, diskussions_id):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")

		cherrypy.Application.db.delete_diskussion(themen_id, diskussions_id)

		raise cherrypy.HTTPRedirect("/diskussionen/index/" + themen_id)

	@cherrypy.expose
	def edit(self, themen_id, diskussions_id, **kwargs):
		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return cherrypy.Application.view.error("403")

		diskussion = cherrypy.Application.db.load_diskussion(diskussions_id)

		if "name" in kwargs and "beschreibung" in kwargs:
			cherrypy.Application.db.edit_diskussion(kwargs["name"], kwargs["beschreibung"], diskussions_id)
			raise cherrypy.HTTPRedirect("/diskussionen/index/" + themen_id)

		template = Template(filename="content/diskussionen/edit.html")
		return template.render(diskussion=diskussion, themen_id=themen_id, diskussions_id=diskussions_id)

# EOF
