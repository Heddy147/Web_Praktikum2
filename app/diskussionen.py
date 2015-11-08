# coding: utf-8
import cherrypy
import json
import collections
from mako.template import Template
from cherrypy import request
from app import database

class Diskussionen_cl(object):

	db = None

	@cherrypy.expose
	def __init__(self):
		self.db = database.Database_cl()

	@cherrypy.expose
	def index(self, themen_id):
		diskussionen = self.db.load_diskussionen(themen_id)

		template = Template(filename="content/diskussionen/index.html")
		return template.render(diskussionen=diskussionen)

# EOF
