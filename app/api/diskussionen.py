import cherrypy
import json


class Diskussionen:

	exposed = True

	@cherrypy.tools.accept(media='plain/text')
	def POST(self, themen_id):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_admin():

			if "name" in jsonContent and "beschreibung" in jsonContent:
				cherrypy.Application.db.create_diskussion(themen_id, jsonContent["name"], jsonContent["beschreibung"])
				return "true"

			return "false_error"
		else:
			return "false_not_admin"

	def PUT(self, themen_id):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		diskussions_id = jsonContent["id"]

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_admin():
			if "name" in jsonContent and "beschreibung" in jsonContent:
				cherrypy.Application.db.edit_diskussion(jsonContent["name"], jsonContent["beschreibung"], diskussions_id)
				return "true"

			return "false_error"
		else:
			return "false_not_admin"

# EOF
