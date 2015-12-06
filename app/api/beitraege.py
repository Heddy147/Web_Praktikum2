import cherrypy
import json


class Beitraege:

	exposed = True

	def GET(self, id=None):

		if id == None:
			print("Nichts")
		else:
			print(id)

		return id

	@cherrypy.tools.accept(media='plain/text')
	def POST(self, diskussions_id):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		print(jsonContent)

		cherrypy.Application.user.user_logged_in()
		if cherrypy.Application.user.is_logged_in():
			if "text" in jsonContent and "titel" in jsonContent:
				cherrypy.Application.db.create_beitrag(diskussions_id, jsonContent["text"], jsonContent["titel"])
				# Rueckgabe von: Alles okay
				return "okay"

			# return template.render(diskussions_id=diskussions_id)
			# Rueckgabe von: Alles scheisse!
			return "not_okay"
		else:
			return "not_okay"
			# return cherrypy.Application.view.error("403")
			# Rueckgabe von: Berechtigungsfehler

	def PUT(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		data = jsonContent['data']
		id = jsonContent['id']


# EOF
