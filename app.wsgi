import sys
sys.path = ['/var/hda/web-apps/remotestick/html/'] + sys.path
import os, bottle
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

import remotestickserver
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
