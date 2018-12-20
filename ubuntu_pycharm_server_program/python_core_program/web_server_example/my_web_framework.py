#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
# from my_web_server import HTTPServer


HTML_ROOT_DIR = "./html"  # the server root directory
"""
framework using:

app = Application()
http_server = HTTPServer(app)
http_server.bind()
http_server.start()

    app(env, start_response)

"""


class Application(object):
    """Framework main program, it's use for alls"""
    def __init__(self, urls):
        # setting urls info
        self.urls = urls

    def __call__(self, env, start_response):
        # find user need path
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            # need static file
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")

            except IOError:
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "Not Found"
            else:
                # response some info
                file_data = file.read()
                file.close()

                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url, handler in self.urls:
            # match running program
            if path == url:
                return handler(env, start_response)
        # 404 judge -- don't find url path
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "Not Found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello itcast"


def say_haha(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello haha"


urls = [
    ("/ctime", show_ctime),
    ("/sayhello", say_hello),
    ("/sayhaha", say_haha),
    ("/", show_ctime)

]

app = Application(urls)

# if __name__ == '__main__':
#
#     urls = [
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello),
#         ("/sayhaha", say_haha),
#         ("/", show_ctime)
#
#     ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
