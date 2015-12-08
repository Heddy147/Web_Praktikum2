# coding: utf-8
import json
import cherrypy
import time


class Database_cl(object):

	def __init__(self):
		pass

	def load_user(self):
		user_file = open("data/user.json", "r")
		user_data = json.load(user_file)

		return user_data

	def create_user(self, username, password, rolle, diskussionen):
		users = self.load_user()
		if username in users:
			return False

		users[username] = {
			"password": password,
			"rolle": rolle,
			"diskussionen": diskussionen
		}

		self.save_users_file(users)

		return True

	def edit_user(self, old_user, username, password, rolle, diskussionen):
		self.delete_user(old_user)

		user = self.load_user()
		if username in user:
			return False

		user[username] = {
			"password": password,
			"rolle": rolle,
			"diskussionen": diskussionen
		}

		self.save_users_file(user)
		return True


	def delete_user(self, username):
		users = self.load_user()
		if username in users:
			del users[username]
			self.save_users_file(users)

	def save_users_file(self, new_content):
		usersFile = open("data/user.json", "w")
		json.dump(new_content, usersFile)

	def sort_themen(self, item):
		return item[1]['name']

	def load_thema(self, thema_id):
		themen = self.load_themen(False)

		if thema_id in themen:
			return themen[thema_id]

		return {}

	def load_themen(self, doSort=True):
		themen_file = open("data/themen.json", "r")
		themen_data = json.load(themen_file)

		if(doSort):
			themen_data = sorted(themen_data.items(), key=self.sort_themen)

		return themen_data

	def edit_thema(self, name, beschreibung, thema_id):
		themen = self.load_themen(False)

		thema = {
			"name": name,
			"beschreibung": beschreibung
		}

		for t_id in themen:
			if t_id == str(thema_id):
				themen[t_id] = thema

		self.save_themen_file(themen)

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

	def get_themen_id_of_diskussion(self, diskussion_id):
		diskussionen = self.load_diskussionen(None, False)

		for t_id in diskussionen:
			for d_id in diskussionen[t_id]:
				if(d_id == diskussion_id):
					return t_id

		return 0

	def load_diskussion(self, diskussions_id):
		diskussionen = self.load_diskussionen(None, False)

		for t_id in diskussionen:
			if diskussions_id in diskussionen[t_id]:
				return diskussionen[t_id][diskussions_id]

		return {}

	def edit_diskussion(self, name, beschreibung, diskussions_id):
		diskussions_id = str(diskussions_id)
		diskussion = self.load_diskussion(diskussions_id)

		diskussion["name"] = name
		diskussion["beschreibung"] = beschreibung

		self.save_diskussion(diskussions_id, diskussion)

	def delete_diskussion(self, themen_id, diskussions_id=None):
		diskussionen = self.load_diskussionen(None, False)

		if diskussions_id == None and themen_id in diskussionen:
			for d_id in diskussionen[themen_id]:
				self.delete_beitrag(d_id)
				diskussionen[themen_id][d_id]["deleted"] = True
			self.save_diskussionen_file(diskussionen)
		elif themen_id in diskussionen and diskussions_id in diskussionen[themen_id]:
			self.delete_beitrag(diskussions_id)
			diskussionen[themen_id][diskussions_id]["deleted"] = True
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

	def load_beitrag(self, beitrags_id):
		beitraege = self.load_beitraege()

		for d_id in beitraege:
			for beitrag in beitraege[d_id]:
				if beitrag[0] == beitrags_id:
					return beitrag[1]

		return {}

	def create_beitrag(self, diskussions_id, text="Text", titel="Titel"):
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
			"titel": titel,
			"text": text,
			"user": cherrypy.Application.user.user,
			"time": time.time()
		}

		self.save_beitraege_file(beitraege)

	def delete_beitrag(self, diskussions_id, beitrags_id=None):
		beitraege = self.load_beitraege(None, False)

		if beitrags_id == None and diskussions_id in beitraege:
			for b_id in beitraege[diskussions_id]:
				beitraege[diskussions_id][b_id]["deleted"] = True

			self.save_beitraege_file(beitraege)
		elif diskussions_id in beitraege and beitrags_id in beitraege[diskussions_id]:
			beitraege[diskussions_id][beitrags_id]["deleted"] = True
			self.save_beitraege_file(beitraege)

	def edit_beitrag(self, beitrags_id, diskussions_id, text, titel):
		beitraege = self.load_beitraege(None, False)

		for d_id in beitraege:
			for b_id in beitraege[d_id]:
				if b_id == str(beitrags_id):
					beitraege[d_id][b_id]['titel'] = titel
					beitraege[d_id][b_id]['text'] = text
		# beitraege[diskussions_id][beitrags_id]['titel'] = titel
		# beitraege[diskussions_id][beitrags_id]['text'] = text

		self.save_beitraege_file(beitraege)

	def save_beitraege_file(self, new_content):
		beitraegeFile = open("data/beitraege.json", "w")
		json.dump(new_content, beitraegeFile)
# EOF
