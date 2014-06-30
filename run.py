import os
import tornado.ioloop
import tornado.web

class MyFileHandler(tornado.web.StaticFileHandler):
    def initialize(self, path):
        self.dirname, self.filename = os.path.split(path)
        super(MyFileHandler, self).initialize(self.dirname)
    def get(self, path = None, include_body = True):
        self.set_header('Content-Type', 'text/javascript')
        super(MyFileHandler, self).get(self.filename, include_body)

app = tornado.web.Application([
    (r'/final\.json', MyFileHandler, {'path': './data/worldCupFinals.json'})
])

app.listen(8888)
tornado.ioloop.IOLoop.current().start()
