# coding: utf-8
import os
import cherrypy
from app import application, module, database, diskussionen, themen, beitrag
from cherrypy.lib import auth_basic
# --------------------------------------

db = database.Database_cl()
application.user = None

def validate_password(realm, username, password):
	users = db.load_user()
	if username in users and users[username]["password"] == password:
		application.user = users[username]
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

	cherrypy.tree.mount(application.Application_cl(), '/', {"/": {}})

	cherrypy.tree.mount(diskussionen.Diskussionen_cl(), '/diskussionen', {'/': {}})
	cherrypy.tree.mount(themen.Themen_cl(), '/themen', {'/': {}})
	cherrypy.tree.mount(beitrag.Beitrag_cl(), '/beitrag', {'/': {}})

	# Start server
	cherrypy.engine.start()
	cherrypy.engine.block()

# --------------------------------------
if __name__ == '__main__':
	# --------------------------------------
	main()
# EOF