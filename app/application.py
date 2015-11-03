# coding: utf-8
import cherrypy
import json
import collections
# --------------------------------------


class Application_cl(object):
	# --------------------------------------
	# ----------------------------------
	def __init__(self):
		# --------------------------------------
		# constructor
		pass
		# --------------------------------------
	# Methode "module" definieren

	def sortBySemester(self, json):
		return int(json['semester'])

	def module(self):
		# --------------------------------------
		# HTML-Code
		markup = """
		<html>
			<head>
				<title>Module</title>
				<script src="js/main.js"></script>
				<link rel="stylesheet" type="text/css" href="css/main.css" />
			</head>
			<body>
				<table id="sort-by-kuerzel">
					<tr>
						<th>Kürzel</th>
						<th>Bezeichnung</th>
						<th>Studiengang</th>
						<th>Semester</th>
					</tr>
		"""
		# Datei "module.json" im Lesemodus oeffnen
		json_data = open("data/module.json", "r")
		data = json.load(json_data)
		data3 = {}
		data2 = collections.OrderedDict(sorted(data.items()))

		for key in data2:
			markup += """
			<tr>
				<td>""" + data2[key]['kuerzel'] + """</td>
				<td>""" + data2[key]['bezeichnung'] + """</td>
				<td>""" + data2[key]['studiengang'] + """</td>
				<td>""" + str(data2[key]['semester']) + """</td>
			</tr>
			"""
			data3[data2[key]['semester']] = data2[key]

		markup += """
				</table>
				<table id="sort-by-semester">
					<tr>
						<th>Kürzel</th>
						<th>Bezeichnung</th>
						<th>Studiengang</th>
						<th>Semester</th>
					</tr>
		"""

		data3 = collections.OrderedDict(sorted(data3.items()))

		for key in data3:
			markup += """
			<tr>
				<td>""" + data3[key]['kuerzel'] + """</td>
				<td>""" + data3[key]['bezeichnung'] + """</td>
				<td>""" + data3[key]['studiengang'] + """</td>
				<td>""" + str(data3[key]['semester']) + """</td>
			</tr>
			"""

		markup += """
				</table>
				<button onclick="sortBySemester();" id="sort-by-semester">Nach Semester sortieren</button>
				<button onclick="sortByKuerzel();" id="sort-by-kuerzel">Nach Kürzel sortieren</button>
			</body>
		</html>
		"""

		# Inhalt von Datei zurueckgeben
		return markup

	module.exposed = True
	# --------------------------------------

	def newFunction(self):
		daten = "lol"
	newFunction.exposed = True

	def	default(self, *arglist, **kwargs):
		# --------------------------------------
		msg_s =	"unbekannte Anforderung: " + \
			str(arglist) + \
			'' + \
			str(kwargs)

		raise cherrypy.HTTPError(404, msg_s)

	default.exposed = True
# EOF
