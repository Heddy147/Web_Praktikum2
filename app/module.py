# coding: utf-8
import cherrypy
from mako.template import Template
from app import database

class Module_cl(object):

	@cherrypy.expose
	def __init__(self):
		pass

	@cherrypy.expose
	def default(self, *arglist, **kwargs):
		return "jo"

	@cherrypy.expose
	def test(self, *arglist, **kwargs):
		db = database.Database_cl()
		themen = db.loadThemen()

		print(themen)

		mytemplate = Template(filename="content/module/test.html")
		return mytemplate.render(themen=themen)

# EOF
