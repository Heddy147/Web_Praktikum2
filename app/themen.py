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
	def view(self):
		themen = self.db.loadThemen()

		template = Template(filename="content/themen/view.html")
		return template.render(themen=themen)

# EOF
