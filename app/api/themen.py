import cherrypy
import json


class Themen:

	exposed = True

	def GET(self, id=None):

		if id == None:
			print("Nichts")
		else:
			print(id)

		return id

	@cherrypy.tools.accept(media='plain/text')
	def POST(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_admin():
			if "name" in jsonContent and "beschreibung" in jsonContent:
				cherrypy.Application.db.create_thema(jsonContent["name"], jsonContent["beschreibung"])
				# Rueckgabe von: Alles okay
				return "okay"

			# return template.render(themen_id=themen_id)
			# Rueckgabe von: Alles scheisse!
			return "not_okay"
		else:
			return "not_okay"
			# return cherrypy.Application.view.error("403")
			# Rueckgabe von: Berechtigungsfehler

	def PUT(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		themen_id = jsonContent['id']

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_admin():
			if "name" in jsonContent and "beschreibung" in jsonContent:
				cherrypy.Application.db.edit_thema(jsonContent["name"], jsonContent["beschreibung"], themen_id)
				return "true"

			return "false_error"
		else:
			return "false_not_logged_in"


# EOF
