import cherrypy
import os.path
from scrape import nScrape,redis_inst,keys
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('html'))
entries = ['entry 0',
            'entry 1',
            'entry 2',
            'entry 3',
            'entry 4',
            'entry 5',
            'entry 6',
            'entry 7',
            'entry 8',
            'entry 9']

class HomePage:

    
    @cherrypy.expose
    def index(self):
        nScrape()
        data_to_render = redis_inst
        tmpl = env.get_template('index.html')
        return tmpl.render(redis_data = data_to_render,entries = entries, keys = keys)
    

root = HomePage()

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 3000)),
}
}
# config_file = os.path.join(os.path.dirname(__file__), 'server.conf')

if __name__ == '__main__':

    cherrypy.quickstart(root, config = config)
