import cherrypy
import json


class Beitraege:

	exposed = True

	@cherrypy.tools.accept(media='plain/text')
	def POST(self, diskussions_id):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_logged_in():
			if "text" in jsonContent and "titel" in jsonContent:
				cherrypy.Application.db.create_beitrag(diskussions_id, jsonContent["text"], jsonContent["titel"])
				return "true"

			return "false_error"
		else:
			return "false_not_logged_in"

	def PUT(self, diskussions_id):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		beitrags_id = jsonContent["id"]

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_logged_in():
			if cherrypy.Application.user.is_editor_of_diskussion(diskussions_id) or (self.is_letzter_beitrag(diskussions_id, beitrags_id) and self.is_bearbeiter(self.get_letzter_beitrag(diskussions_id))):
				if "text" in jsonContent and "titel" in jsonContent:
					cherrypy.Application.db.edit_beitrag(beitrags_id, diskussions_id, jsonContent["text"], jsonContent["titel"])
					return "true"

				return "false_error"
			else:
				return "false_rights"
		else:
			return "false_not_logged_in"


	def is_bearbeiter(self, beitrag):
		cherrypy.Application.user.user_logged_in()
		return beitrag[1]["user"] == cherrypy.Application.user.user

	def is_letzter_beitrag(self, diskussions_id, beitrags_id):
		letzterBeitrag = self.get_letzter_beitrag(diskussions_id)

		return letzterBeitrag[0] == beitrags_id

	def get_letzter_beitrag(self, diskussions_id):
		beitraege = cherrypy.Application.db.load_beitraege(diskussions_id)
		return beitraege[len(beitraege) - 1]
# EOF
