# coding: utf-8
import os
import cherrypy
from app import application, module, database, diskussion, thema, beitrag
from cherrypy.lib import auth_basic
# --------------------------------------

db = database.Database_cl()


def validate_password(realm, username, password):
	users = db.loadUser()
	if username in users and users[username]["password"] == password:
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

	config_file = "server.conf"
	if os.path.dirname(config_file) == False:
		config_file = None

	# disable autoreload and timeout_monitor
	cherrypy.engine.autoreload.unsubscribe()
	cherrypy.engine.timeout_monitor.unsubscribe()
	# Static content config
	static_config = {
		'/': {
			'tools.staticdir.root': current_dir,
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './content',
			'tools.staticdir.index': 'index.html'
		},
		'/module': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	}

	cherrypy.tree.mount(None, '/', config_file)

	# Mount static content handler
	cherrypy.tree.mount(module.Module_cl(), '/module', {
		'/': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	})

	# Mount static content handler
	cherrypy.tree.mount(diskussion.Diskussion_cl(), '/diskussion', {
		'/': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	})

	# Mount static content handler
	cherrypy.tree.mount(thema.Thema_cl(), '/thema', {
		'/': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	})

	# Mount static content handler
	cherrypy.tree.mount(beitrag.Beitrag_cl(), '/beitrag', {
		'/': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	})

	# Mount static content handler
	cherrypy.tree.mount(application.Application_cl(), '/application', {
		'/': {
			'tools.auth_basic.on': True,
			'tools.auth_basic.realm': 'localhost',
			'tools.auth_basic.checkpassword': validate_password
		}
	})

	# Start server
	cherrypy.engine.start()
	cherrypy.engine.block()

# --------------------------------------
if __name__ == '__main__':
	# --------------------------------------
	main()
# EOF