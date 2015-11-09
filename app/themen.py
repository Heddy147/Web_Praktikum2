# coding: utf-8

import cherrypy
from mako.template import Template
from app import database


class Themen_cl(object):

	db = None

	def __init__(self):
		self.db = database.Database_cl()
		pass

	@cherrypy.expose
	def index(self):
		themen = self.db.load_themen()

		template = Template(filename="content/themen/index.html")
		return template.render(themen=themen)

	@cherrypy.expose
	def delete(self, themen_id):
		self.db.delete_thema(themen_id)

		raise cherrypy.HTTPRedirect("/themen/index")

	@cherrypy.expose
	def create(self, **kwargs):
		if "name" in kwargs and "beschreibung" in kwargs:
			self.db.create_thema(kwargs["name"], kwargs["beschreibung"])
			raise cherrypy.HTTPRedirect("/themen/index")

		template = Template(filename="content/themen/create.html")
		return template.render()

	@cherrypy.expose
	def edit(self, thema_id, **kwargs):
		if "name" in kwargs and "beschreibung" in kwargs:
			self.db.edit_thema(kwargs["name"], kwargs["beschreibung"], thema_id)
			raise cherrypy.HTTPRedirect("/themen/index")

		thema = self.db.load_thema(thema_id)

		template = Template(filename="content/themen/edit.html")
		return template.render(thema=thema)

# EOF
