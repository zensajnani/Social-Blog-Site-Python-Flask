import os
import sys

# sys.path.insert(0, "/webapps/social_blog_site")
#
# import app
# application = app

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

# Add project top-dir to path (since it has no __init__.py)
sys.path.append(PROJECT_DIR + '/src/')
#
# def application(environ, start_response):
#     output = 'Welcome to your mod_wsgi website! It uses:\n\nPython %s' % sys.version
#     output += '\nWSGI version: %s' % str(environ['mod_wsgi.version'])
#     output += '\nPath: ' + str(sys.path)
#     response_headers = [
#         ('Content-Length', str(len(output))),
#         ('Content-Type', 'text/plain'),
#     ]
#
#     start_response('200 OK', response_headers)
#
#     return [bytes(output, 'utf-8')]

from .htdocs import app as application
