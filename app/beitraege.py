# coding: utf-8
import cherrypy
from mako.template import Template
from app import database


class Beitraege_cl(object):

	db = None

	@cherrypy.expose
	def __init__(self):
		self.db = database.Database_cl()
		pass

	@cherrypy.expose
	def index(self, diskussions_id):
		beitraege = self.db.load_beitraege(diskussions_id)
		diskussion = self.db.load_diskussion(diskussions_id)

		template = Template(filename="content/beitraege/index.html")
		return template.render(beitraege=beitraege, diskussions_id=diskussions_id, diskussion=diskussion)

	@cherrypy.expose
	def delete(self, diskussions_id, beitrags_id):
		self.db.delete_beitrag(diskussions_id, beitrags_id)

		raise cherrypy.HTTPRedirect("/beitraege/index/" + diskussions_id)

	@cherrypy.expose
	def create(self, diskussions_id, **kwargs):
		if "text" in kwargs:
			self.db.create_beitrag(diskussions_id, kwargs["text"])
			raise cherrypy.HTTPRedirect("/beitraege/index/" + diskussions_id)

		template = Template(filename="content/beitraege/create.html")
		return template.render(diskussions_id=diskussions_id)

# EOF
