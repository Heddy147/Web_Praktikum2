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
		cherrypy.Application.user.user_logged_in()

		if cherrypy.Application.user.is_editor_of_diskussion(diskussions_id) or (self.is_letzter_beitrag(diskussions_id, beitrags_id) and self.is_bearbeiter(self.get_letzter_beitrag(diskussions_id))):
			self.db.delete_beitrag(diskussions_id, beitrags_id)

			raise cherrypy.HTTPRedirect("/beitraege/index/" + diskussions_id)
		else:
			return cherrypy.Application.view.error("403")

	@cherrypy.expose
	def create(self, diskussions_id, **kwargs):
		cherrypy.Application.user.user_logged_in()
		if "text" in kwargs:
			self.db.create_beitrag(diskussions_id, kwargs["text"])
			raise cherrypy.HTTPRedirect("/beitraege/index/" + diskussions_id)

		template = Template(filename="content/beitraege/create.html")
		return template.render(diskussions_id=diskussions_id)

	def is_bearbeiter(self, beitrag):
		cherrypy.Application.user.user_logged_in()
		return beitrag[1]["user"] == cherrypy.Application.user.user

	def is_letzter_beitrag(self, diskussions_id, beitrags_id):
		letzterBeitrag = self.get_letzter_beitrag(diskussions_id)

		return letzterBeitrag[0] == beitrags_id

	def get_letzter_beitrag(self, diskussions_id):
		beitraege = cherrypy.Application.db.load_beitraege(diskussions_id)
		return beitraege[len(beitraege) - 1]

	@cherrypy.expose
	def edit(self, diskussions_id, beitrags_id, **kwargs):
		beitrag = self.db.load_beitrag(beitrags_id)
		print beitrag["text"]
		if "text" in kwargs:
			self.db.edit_beitrag(beitrags_id, kwargs["text"])
			raise cherrypy.HTTPRedirect("/beitraege/index/" + diskussions_id)

		template = Template(filename="content/beitraege/edit.html")
		return template.render(beitrag=beitrag, diskussions_id=diskussions_id)

# EOF
