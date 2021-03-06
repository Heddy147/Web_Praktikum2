# coding: utf-8
import os
import cherrypy
import imp
from app import application, diskussionen, themen, beitraege, login, database, user, view, benutzer
# from app.api import beitraege as beitraege_api
# from app.api import themen as themen_api
beitraege_api = imp.load_source("app.api", "app/api/beitraege.py")
benutzer_api = imp.load_source("app.api", "app/api/benutzer.py")
themen_api = imp.load_source("app.api", "app/api/themen.py")
diskussionen_api = imp.load_source("app.api", "app/api/diskussionen.py")

def validate_password(realm, username, password):
	users = application.db.load_user()
	if username in users and users[username]["password"] == password:
		application.user = username
		return True
	return False


def main():
	# --------------------------------------
	# Get current directory
	try:
		current_dir = os.path.dirname(os.path.abspath(__file__))
	except:
		current_dir = os.path.dirname(os.path.abspath(sys.executable))

	cherrypy.Application.currentDir = current_dir

	# disable autoreload and timeout_monitor
	cherrypy.engine.autoreload.unsubscribe()
	cherrypy.engine.timeout_monitor.unsubscribe()

	cherrypy.tree.mount(application.Application_cl(), '/', {"/": {}})
	css_handler = cherrypy.tools.staticdir.handler(section="/", dir='/content/css')
	cherrypy.tree.mount(css_handler, '/css', {
		'/': {
			'tools.staticdir.root': current_dir,
			'tools.staticdir.on': True,
			'tools.staticdir.dir': 'content/css'
		}
	})
	js_handler = cherrypy.tools.staticdir.handler(section="/", dir='/content/js')
	cherrypy.tree.mount(js_handler, '/js', {
		'/': {
			'tools.staticdir.root': current_dir,
			'tools.staticdir.on': True,
			'tools.staticdir.dir': 'content/js'
		}
	})

	cherrypy.tree.mount(diskussionen.Diskussionen_cl(), '/diskussionen', {
		'/': {
			'tools.staticdir.root': current_dir
		}
	})
	cherrypy.tree.mount(themen.Themen_cl(), '/themen', {
		'/': {
			'tools.staticdir.root': current_dir
		}
	})
	cherrypy.tree.mount(beitraege.Beitraege_cl(), '/beitraege', {
		'/': {
			'tools.staticdir.root': current_dir
		}
	})
	cherrypy.tree.mount(login.Login_cl(), '/login', {
		'/': {
			'tools.staticdir.root': current_dir
		}
	})
	cherrypy.tree.mount(benutzer.Benutzer_cl(), '/benutzer', {
		'/': {
			'tools.staticdir.root': current_dir
		}
	})
	cherrypy.tree.mount(beitraege_api.Beitraege(), '/api/beitraege', {
		'/': {
			'tools.staticdir.root': current_dir,
			'request.dispatch': cherrypy.dispatch.MethodDispatcher()
		}
	})
	cherrypy.tree.mount(benutzer_api.Benutzer(), '/api/benutzer', {
		'/': {
			'tools.staticdir.root': current_dir,
			'request.dispatch': cherrypy.dispatch.MethodDispatcher()
		}
	})
	cherrypy.tree.mount(themen_api.Themen(), '/api/themen', {
		'/': {
			'tools.staticdir.root': current_dir,
			'request.dispatch': cherrypy.dispatch.MethodDispatcher()
		}
	})
	cherrypy.tree.mount(diskussionen_api.Diskussionen(), '/api/diskussionen', {
		'/': {
			'tools.staticdir.root': current_dir,
			'request.dispatch': cherrypy.dispatch.MethodDispatcher()
		}
	})

	cherrypy.Application.db = database.Database_cl()
	cherrypy.Application.user = user.User_cl()
	cherrypy.Application.view = view.View_cl()

	# Start server
	cherrypy.engine.start()
	cherrypy.engine.block()

# --------------------------------------
if __name__ == '__main__':
	# --------------------------------------
	main()
# EOF