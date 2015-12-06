import cherrypy
import json

class Benutzer:

	exposed = True

	def POST(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)

		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return 'false_rights'

		if "diskussionen" not in jsonContent:
			jsonContent["diskussionen"] = []

		if "username" in jsonContent and "password" in jsonContent and "rolle" in jsonContent:
			if cherrypy.Application.db.create_user(jsonContent["username"], jsonContent["password"], jsonContent["rolle"], jsonContent["diskussionen"]):
				return "true"
			else:
				return 'false_error'

		return 'false_error'

	def PUT(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)

		cherrypy.Application.user.user_logged_in()
		if not cherrypy.Application.user.is_admin():
			return 'false_rights'

		if "diskussionen" not in jsonContent:
			jsonContent["diskussionen"] = []

		if "username" in jsonContent and "password" in jsonContent and "rolle" in jsonContent:
			if cherrypy.Application.db.edit_user(jsonContent['benutzername'], jsonContent["username"], jsonContent["password"], jsonContent["rolle"], jsonContent["diskussionen"]):
				return "true"
			else:
				return 'false_error'

		user = cherrypy.Application.db.load_user()

		return 'false_error'

# EOF
