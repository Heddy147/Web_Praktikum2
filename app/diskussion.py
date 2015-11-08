# coding: utf-8
import cherrypy
import json
import collections
from mako.template import Template
from cherrypy import request


class Diskussion_cl(object):

	@cherrypy.expose
	def __init__(self):
		pass

	@cherrypy.expose
	def default(self, **kwargs):
		markup = ""

		# --------------------------------------
		# HTML-Code

		markup += """
		<html>
			<head>
				<title>Module</title>
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
				<script src="../content/js/main.js"></script>
				<link rel="stylesheet" type="text/css" href="../content/css/main.css" />
				<script>
					$(document).ready(function () {
						diskussionClicked();
					});
				</script>
			</head>
			<body>
			"""
		markup += """
				<h1>Diskussionen</h1>
				<table id="sort-by-kuerzel">
					<tr>
						<th>Titel</th>
						<th>Beschreibung</th>
					</tr>
		"""
		# Datei "module.json" im Lesemodus oeffnen
		json_data = open("data/diskussion.json", "r")
		data = json.load(json_data)
		data2 = collections.OrderedDict(sorted(data.items()))

		# Inhalt von Datei zurueckgeben
		if request.method == 'GET' and 'id' in request.params:
			for key in data2.keys():
				print request.params['id'] + """==""" + data2[key]['key']

				if request.params['id'] == data2[key]['key']:
					markup += """
					<tr id='""" + key + """'>
						<td>""" + data2[key]['titel'] + """</td>
						<td>""" + data2[key]['beschreibung'] + """</td>
					</tr>
					"""

		markup += """
				</table>
			</body>
		</html>
		"""

		return markup

	@cherrypy.expose
	def test(self, **kwargs):
		# print(arglist)
		# print(kwargs)

		if request.method == 'POST' and 'wasGeht' in request.params:
			print request.params['wasGeht']

		mytemplate = Template(filename="content/module/test.html")
		return mytemplate.render(placeholder="Ihr Name123")

	@cherrypy.expose
	def diskussion(self):
		return "deskussion"

# EOF
