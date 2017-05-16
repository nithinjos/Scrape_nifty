import cherrypy
import os.path
import time
from scrape import nScrape,redis_inst,keys
from jinja2 import Environment, FileSystemLoader
from cherrypy.process.plugins import BackgroundTask
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


# class Scraper(Thread):
#     def __init__(self):
#         Thread.__init__(self, delay)
#         self.delay = delay

#     def run(self):
#         while True:
#             time.sleep(self.delay)
#             nScrape()

    


nScrape()
BackgroundTask(300 , nScrape, bus = cherrypy.engine).start()

class HomePage:   
    @cherrypy.expose
    def index(self):
        data_to_render = redis_inst
        tmpl = env.get_template('index.html')
        return tmpl.render(redis_data = data_to_render,entries = entries, keys = keys)
    

root = HomePage()

config = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 3000)),
        'engine.autoreload.on': True,
}
}
# config_file = os.path.join(os.path.dirname(__file__), 'server.conf')

if __name__ == '__main__':

    cherrypy.quickstart(root, config = config)
