import falcon
from klawisz import Klawisz
from jinja2 import Template

CHANNEL = 17
SECONDS = 5

KLAWISZ = Klawisz(CHANNEL)
 

class Lokaj:
    template_name = "lokaj.html"

    def on_get(self, req, resp):
        resp.body = self.template.render()
        resp.status = falcon.HTTP_200
        resp.set_header('Content-Type', 'text/html')
    
    @property
    def template(self):
        return Template(open(self.template_name).read())
        
 

class Otwórz:
    def on_get(self, req, resp):
        resp.body = """otwieram"""
        KLAWISZ.otwórz(SECONDS)

 
api = falcon.API()
api.add_route('/', Lokaj())
api.add_route('/otwórz/', Otwórz())
