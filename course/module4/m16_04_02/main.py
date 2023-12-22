import urllib.parse
import json
import socket
import mimetypes
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from threading import Thread

from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path()
BUFFER_SIZE = 1024
HTTP_PORT = 8080
HTTP_HOST = '0.0.0.0'
SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = 4000

jinja = Environment(loader=FileSystemLoader('templates'))


class GoitFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case '/':
                self.send_html('index.html')
            case '/contact':
                self.send_html('contact.html')
            case '/blog':
                self.render_template('blog.jinja')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('404.html')

    def do_POST(self):
        size = self.headers.get('Content-Length')
        data = self.rfile.read(int(size))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(data, (SOCKET_HOST, SOCKET_PORT))
        client_socket.close()

        self.send_response(302)
        self.send_header('Location', '/contact')
        self.end_headers()

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def render_template(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('storage/db.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        template = jinja.get_template(filename)
        message = None  # "Hello Serhiy!"
        html = template.render(blogs=data, message=message)
        self.wfile.write(html.encode())

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, *_ = mimetypes.guess_type(filename)
        self.send_header('Content-type', mime_type or 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())


def save_data_from_form(data):
    parse_data = urllib.parse.unquote_plus(data.decode())
    try:
        parse_dict = {key: val for key, val in [pair.split('=') for pair in parse_data.split('&')]}
        with open('data/data.json', 'a', encoding='utf-8') as file:
            json.dump(parse_dict, file, ensure_ascii=False, indent=4)
    except ValueError as err:
        logging.error(err)
    except OSError as err:
        logging.error(err)


def run_socket_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    logging.info(f'Starting socket server on {host}:{port}')
    try:
        while True:
            msg, addr = server_socket.recvfrom(BUFFER_SIZE)
            logging.info(f'Socket received message from {addr}: {msg}')
            save_data_from_form(msg)
    except KeyboardInterrupt:
        pass
    finally:
        server_socket.close()


def run_http_server(host, port):
    address = (host, port)
    http_server = HTTPServer(address, GoitFramework)
    logging.info(f'Starting http server on {host}:{port}')
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.server_close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

    http_server = Thread(target=run_http_server, args=(HTTP_HOST, HTTP_PORT))
    http_server.start()

    socket_server = Thread(target=run_socket_server, args=(SOCKET_HOST, SOCKET_PORT))
    socket_server.start()
