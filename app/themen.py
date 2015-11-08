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
# EOF
