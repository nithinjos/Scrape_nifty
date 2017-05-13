import cherrypy
import os.path
from scrape import nScrape,redis_inst
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('html'))

class HomePage:

    
    @cherrypy.expose
    def index(self):
        nScrape()
        data_to_render = redis_inst
        tmpl = env.get_template('index.html')
        return tmpl.render(data = data_to_render)
    

root = HomePage()

config_file = os.path.join(os.path.dirname(__file__), 'server.conf')

if __name__ == '__main__':

    cherrypy.quickstart(root, config = config_file)