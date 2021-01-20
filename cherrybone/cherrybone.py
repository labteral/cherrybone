#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
import logging
import cherrypy
import multiprocessing
import json

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)-15s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Server:
    def __init__(self,
                 app,
                 port=None,
                 path=None,
                 host=None,
                 threads=None,
                 max_body_bytes=None,
                 max_header_bytes=None,
                 max_threads=None,
                 max_queued_connection=None,
                 connection_timeout=None,
                 max_queued_requests=None,
                 request_acceptance_timeout=None,
                 tcp_nodelay=None,
                 shutdown_timeout=None):
        self._app = app

        # https://docs.cherrypy.org/en/latest/pkg/cherrypy._cpserver.html
        self._config = {
            'path': '/' if path is None else path,
            'port': 80 if port is None else port,
            'host': '0.0.0.0' if host is None else host,
            'threads': multiprocessing.cpu_count() if threads is None else threads,
            'max_body_bytes': 1073741824 if max_body_bytes is None else max_body_bytes,
            'max_header_bytes': 1048576 if max_header_bytes is None else max_header_bytes,
            'max_threads': -1 if max_threads is None else max_threads,
            'max_queued_connection': 10 if max_queued_connection is None else max_queued_connection,
            'connection_timeout': 10 if connection_timeout is None else connection_timeout,
            'max_queued_requests': -1 if max_queued_requests is None else max_queued_requests,
            'request_acceptance_timeout': 10 if request_acceptance_timeout is None else request_acceptance_timeout,
            'tcp_nodelay': True if tcp_nodelay is None else tcp_nodelay,
            'shutdown_timeout': 10 if shutdown_timeout is None else shutdown_timeout
        }

        cherrypy.config.update({
            'server.socket_port': self._config['port'],
            'server.socket_host': self._config['host'],
            'server.thread_pool': self._config['threads'],
            'server.thread_pool_max': self._config['max_threads'],
            'server.max_request_body_size': self._config['max_body_bytes'],
            'server.max_request_header_size': self._config['max_header_bytes'],
            'server.socket_queue_size': self._config['max_queued_connection'],
            'server.socket_timeout': self._config['connection_timeout'],
            'server.accepted_queue_size': self._config['max_queued_requests'],
            'server.accepted_queue_timeout': self._config['request_acceptance_timeout'],
            'server.nodelay': self._config['tcp_nodelay'],
            'server.shutdown_timeout': self._config['shutdown_timeout'],
            'engine.autoreload.on': False,
            'checker.on': False,
            'tools.log_headers.on': False,
            'request.show_tracebacks': False,
            'request.show_mismatched_params': False,
            'log.screen': False,
            'engine.SIGHUP': None,
            'engine.SIGTERM': None
        })

    def start(self):
        cherrypy.tree.graft(self._app, self._config['path'])
        logging.info(f'CherryPy config: {json.dumps(self._config, indent=2)}')
        cherrypy.engine.start()

    def stop(self):
        cherrypy.engine.exit()
