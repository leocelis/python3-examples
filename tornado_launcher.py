import tornado
from rest_api import app
from tornado import autoreload
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

sockets = tornado.netutil.bind_sockets(port=5000, backlog=256)
tornado.process.fork_processes(0)
server = HTTPServer(WSGIContainer(app))
server.add_sockets(sockets)
ioloop = IOLoop.instance()
autoreload.start(ioloop)
ioloop.start()
