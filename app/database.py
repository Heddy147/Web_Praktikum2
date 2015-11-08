# coding: utf-8
import cherrypy
import json
import collections


class Database_cl(object):

	def __init__(self):
		pass

	@cherrypy.expose
	def loadUser(self):
		userFile = open("data/user.json", "r")
		userData = json.load(userFile)

		return userData

	@cherrypy.expose
	def loadThemen(self):
		themenFile = open("data/themen.json", "r")
		themenData = json.load(themenFile)

		return themenData

# EOF
