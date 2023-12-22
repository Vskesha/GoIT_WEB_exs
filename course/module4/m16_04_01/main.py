import urllib.parse
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes


BASE_DIR = Path()


class GoitFramework(BaseHTTPRequestHandler):

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case '/':
                self.send_html('index.html')
            case '/contact':
                self.send_html('contact.html')
            case '/blog':
                self.send_html('blog.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('404.html')

    def do_POST(self):
        pass

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mime_type, *_ = mimetypes.guess_type(filename)
        self.send_header('Content-type', mime_type or 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())


def run_server():
    address = ('localhost', 8080)
    http_server = HTTPServer(address, GoitFramework)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.server_close()


if __name__ == '__main__':
    run_server()
