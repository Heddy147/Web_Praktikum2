# coding: utf-8
import json
import time
import operator
import collections
from app import application


class Database_cl(object):

	def __init__(self):
		pass

	def load_user(self):
		user_file = open("data/user.json", "r")
		user_data = json.load(user_file)

		return user_data

	def sort_themen(self, item):
		return item[1]['name']

	def load_themen(self, doSort=True):
		themen_file = open("data/themen.json", "r")
		themen_data = json.load(themen_file)

		if(doSort):
			themen_data = sorted(themen_data.items(), key=self.sort_themen)

		return themen_data

	def create_thema(self, name="Thema", beschreibung="Beschreibung"):
		themen = self.load_themen(False)
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

	def delete_thema(self, themen_id):
		themen = self.load_themen(False)
		del themen[themen_id]
		self.save_themen_file(themen)
		self.delete_diskussion(themen_id)

	def save_themen_file(self, new_content):
		themenFile = open("data/themen.json", "w")
		json.dump(new_content, themenFile)

	def create_diskussion(self, themen_id, name="Diskussion", beschreibung="Beschreibung"):
		diskussionen = self.load_diskussionen(None, False)

		print "themen_id" + str(themen_id) + "name: " + name + "beschreibung: " + beschreibung
		last_diskussions_id = 0

		for t_id in diskussionen:
			for d_id in diskussionen[t_id]:
				if int(d_id) > last_diskussions_id:
					last_diskussions_id = int(d_id)

		last_diskussions_id += 1

		if themen_id not in diskussionen:
			diskussionen[themen_id] = {}

		diskussionen[themen_id][last_diskussions_id] = {
			"name": name,
			"beschreibung": beschreibung,
			"time": time.time()
		}

		self.save_diskussionen_file(diskussionen)

	def sort_diskussionen(self, item):
		return int(item[1]['time'])

	def load_diskussionen(self, themen_id=None, doSort=True):
		diskussionen_file = open("data/diskussionen.json", "r")
		diskussionen_data = json.load(diskussionen_file)

		if(doSort):
			sorted_data = {}

			for t_id in diskussionen_data:
				sorted_diskussionen = sorted(diskussionen_data[t_id].items(), key=self.sort_diskussionen, reverse=True)
				sorted_data[t_id] = sorted_diskussionen

			if themen_id == None:
				return sorted_data

			if themen_id in sorted_data:
				return sorted_data[themen_id]
			else:
				return []

		if themen_id == None:
			return diskussionen_data

		if themen_id in diskussionen_data:
			return diskussionen_data[themen_id]
		else:
			return {}

	def load_diskussion(self, diskussions_id):
		diskussionen = self.load_diskussionen(None, False)

		for t_id in diskussionen:
			if diskussions_id in diskussionen[t_id]:
				return diskussionen[t_id][diskussions_id]

		return {}

	def delete_diskussion(self, themen_id, diskussions_id=None):
		diskussionen = self.load_diskussionen(None, False)

		if diskussions_id == None and themen_id in diskussionen:
			for d_id in diskussionen[themen_id]:
				self.delete_beitrag(d_id)
			del diskussionen[themen_id]
			self.save_diskussionen_file(diskussionen)
		elif themen_id in diskussionen and diskussions_id in diskussionen[themen_id]:
			self.delete_beitrag(diskussions_id)
			del diskussionen[themen_id][diskussions_id]
			self.save_diskussionen_file(diskussionen)

	def save_diskussion(self, diskussions_id, diskussion):
		diskussionen = self.load_diskussionen(None, False)

		for t_id in diskussionen:
			for d_id in diskussionen[t_id]:
				if d_id == diskussions_id:
					diskussionen[t_id][d_id] = diskussion

		self.save_diskussionen_file(diskussionen)

	def save_diskussionen_file(self, new_content):
		diskussionenFile = open("data/diskussionen.json", "w")
		json.dump(new_content, diskussionenFile)

	def sort_beitraege(self, item):
		return int(item[1]['time'])

	def load_beitraege(self, diskussionen_id=None, doSort=True):
		beitraege_file = open("data/beitraege.json", "r")
		beitraege_data = json.load(beitraege_file)

		if(doSort):
			sorted_data = {}

			for d_id in beitraege_data:
				sorted_beitraege = sorted(beitraege_data[d_id].items(), key=self.sort_beitraege)
				sorted_data[d_id] = sorted_beitraege

			if diskussionen_id == None:
				return sorted_data

			if diskussionen_id in sorted_data:
				return sorted_data[diskussionen_id]
			else:
				return []

		if diskussionen_id == None:
			return beitraege_data

		if diskussionen_id in beitraege_data:
			return beitraege_data[diskussionen_id]
		else:
			return {}

	def create_beitrag(self, diskussions_id, text="Text"):
		beitraege = self.load_beitraege(None, False)

		last_beitrags_id = 0

		for d_id in beitraege:
			for b_id in beitraege[d_id]:
				if int(b_id) > last_beitrags_id:
					last_beitrags_id = int(b_id)

		last_beitrags_id += 1

		if diskussions_id not in beitraege:
			beitraege[diskussions_id] = {}

		if len(beitraege[diskussions_id]) == 0:
			diskussion = self.load_diskussion(diskussions_id)
			diskussion['time'] = time.time()
			self.save_diskussion(diskussions_id, diskussion)

		beitraege[diskussions_id][last_beitrags_id] = {
			"text": text,
			"user": application.user,
			"time": time.time()
		}

		self.save_beitraege_file(beitraege)

	def delete_beitrag(self, diskussions_id, beitrags_id=None):
		beitraege = self.load_beitraege(None, False)

		if beitrags_id == None and diskussions_id in beitraege:
			del beitraege[diskussions_id]
			self.save_beitraege_file(beitraege)
		elif diskussions_id in beitraege and beitrags_id in beitraege[diskussions_id]:
			del beitraege[diskussions_id][beitrags_id]
			self.save_beitraege_file(beitraege)

	def save_beitraege_file(self, new_content):
		beitraegeFile = open("data/beitraege.json", "w")
		json.dump(new_content, beitraegeFile)
# EOF
