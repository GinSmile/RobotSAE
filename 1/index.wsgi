import sae
from myApp import app

application = sae.create_wsgi_app(app)