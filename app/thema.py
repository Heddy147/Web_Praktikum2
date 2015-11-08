# coding: utf-8
import cherrypy
import json
import collections
from app import diskussion
from mako.template import Template
from cherrypy import request


class Thema_cl(object):
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
						themaClicked();
					});
				</script>
			</head>
			<body>
				<h1>Themen</h1>
				<table id="sort-by-kuerzel">
					<tr>
						<th>Titel</th>
						<th>Beschreibung</th>
					</tr>
		"""
		# Datei "module.json" im Lesemodus oeffnen
		json_data = open("data/thema.json", "r")
		data = json.load(json_data)
		data2 = collections.OrderedDict(sorted(data.items()))

		for key in data2:
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

		# Inhalt von Datei zurueckgeben

		return markup

	@cherrypy.expose
	def thema(self):
		return "thema"

# EOF
