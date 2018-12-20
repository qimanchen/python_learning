#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import re
import sys

from multiprocessing import Process

HTML_ROOT_DIR = "./html"  # the server root directory
WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""

    def __init__(self, application):
        """ application --> framework class"""
        # server_socket create
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = application

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s] link the server" % (client_address[0], client_address[1]))

            # client process
            client = Process(target=self.handle_client, args=(client_socket,))
            client.start()
            client_socket.close()

    # built
    def start_response(self, status, headers):
        """ """
        # server_headers = [
        #     ("Server", "My Server")
        # ]
        # server_headers + headers

        # get contents for response to client
        # status = "200 OK"
        # headers = [
        #     ("Content-Type", "text/plain")
        # ]
        response_headers = "HTTP/1.1 " \
                           "" + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header

        self.response_headers = response_headers

    def handle_client(self, client_socket):
        """handle client request"""
        request_data = client_socket.recv(1024)
        print(request_data)

        request_lines = request_data.splitlines()

        request_start_line = request_lines[0]
        # match / directory
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w)+ +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env, self.start_response)

        response = self.response_headers + "\r\n" + response_body

        # send response data to browser
        # client_socket.send(response.encode("utf-8"))
        client_socket.send(bytes(response, "utf-8"))

        # close client socket
        # client_socket.close()


def main():
    """ """
    # add find path for dynamic run program
    sys.path.insert(1, WSGI_PYTHON_DIR)
    if len(sys.argv) < 2:
        sys.exit("python my_wev_server.py Module:app")
    # python my_web_server.py my_web_framework:app
    module_name, app_name = sys.argv[1].split(":")
    # module_name = "my_web_framework"
    # app_name = "app"
    m = __import__(module_name)
    app = getattr(m, app_name)

    # create a server
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()


"""
1. http_server = HTTPServer(8000)
2. http_server.start()
3. http
"""

if __name__ == '__main__':
    main()
