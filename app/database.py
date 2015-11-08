# coding: utf-8
import cherrypy
import json
import collections


class Database_cl(object):

	def __init__(self):
		pass

	def load_user(self):
		user_file = open("data/user.json", "r")
		user_data = json.load(user_file)

		return user_data

	def create_thema(self, name="Thema", beschreibung="Beschreibung"):
		themen = self.load_themen()
		last_themen_id = 0

		for t_id in themen:
			if int(t_id) > last_themen_id:
				last_themen_id = int(t_id)

		last_themen_id += 1

		themen[last_themen_id] = {
			"name": name,
			"beschreibung": beschreibung
		}

		self.save_themen_file(themen)

	def save_themen_file(self, new_content):
		themenFile = open("data/themen.json", "w")
		json.dump(new_content, themenFile)

	def load_themen(self):
		themen_file = open("data/themen.json", "r")
		themen_data = json.load(themen_file)

		return themen_data

	def delete_thema(self, themen_id):
		themen = self.load_themen()
		del themen[themen_id]
		self.save_themen_file(themen)
		self.delete_diskussion(themen_id)

	def create_diskussion(self, themen_id, name="Diskussion", beschreibung="Beschreibung"):
		diskussionen = self.load_diskussionen()

		last_diskussions_id = 0

		for t_id in diskussionen:
			for d_id in diskussionen[t_id]:
				if int(d_id) > last_diskussions_id:
					last_diskussions_id = int(d_id)

		last_diskussions_id += 1

		diskussionen[themen_id][last_diskussions_id] = {
			"name": name,
			"beschreibung": beschreibung
		}

		self.save_diskussionen_file(diskussionen)

	def load_diskussionen(self, themen_id=None):
		diskussionen_file = open("data/diskussionen.json", "r")
		diskussionen_data = json.load(diskussionen_file)

		if themen_id == None:
			return diskussionen_data

		if themen_id in diskussionen_data:
			return diskussionen_data[themen_id]
		else:
			return {}

	def delete_diskussion(self, themen_id):
		diskussionen = self.load_diskussionen()

		if themen_id in diskussionen:
			del diskussionen[themen_id]
			self.save_diskussionen_file(diskussionen)
			# hier noch beitraege loeschen

	def save_diskussionen_file(self, new_content):
		diskussionenFile = open("data/diskussionen.json", "w")
		json.dump(new_content, diskussionenFile)
# EOF
