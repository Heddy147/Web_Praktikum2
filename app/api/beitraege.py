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

	@cherrypy.tools.accept(media='application/json')
	def POST(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		print(jsonContent['id'])

		return ''

	def PUT(self):
		content = cherrypy.request.body.read().decode("utf-8")
		jsonContent = json.loads(content)
		data = jsonContent['data']
		id = jsonContent['id']

# EOF
