# coding: utf-8
import cherrypy
from mako.template import Template
from cherrypy import request


class Module_cl(object):

	@cherrypy.expose
	def __init__(self):
		pass

	@cherrypy.expose
	def default(self, *arglist, **kwargs):
		# print("jo")
		# print(kwargs['al'])

		return "module default"

	@cherrypy.expose
	def test(self, *arglist, **kwargs):
		# print(arglist)
		# print(kwargs)

		if request.method == 'POST' and 'wasGeht' in request.params:
			print request.params['wasGeht']

		mytemplate = Template(filename="content/module/test.html")
		return mytemplate.render(placeholder="Ihr Name123")

	@cherrypy.expose
	def benutzerverwaltung(self):
		mytemplate = Template(filename="content/module/benutzerverwaltung.html")
		return mytemplate.render()



# EOF
