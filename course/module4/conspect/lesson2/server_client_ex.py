from threading import Thread
from time import sleep
from http import client
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<!DOCTYPE html>\n'
                         b'<html>\n'
                         b'  <head>\n'
                         b'    <title>First server</title>\n'
                         b'  </head>\n'
                         b'  <body>\n'
                         b'    <h1>Hello, world!</h1>'
                         b'  </body>\n'
                         b'</html>\n')

    def do_POST(self):
        pass


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8001), SimpleHTTPRequestHandler)
    server = Thread(target=httpd.serve_forever)
    server.start()
    sleep(1)

    h1 = client.HTTPConnection('localhost', 8001)
    h1.request('GET', '/')

    res = h1.getresponse()
    print(res.status, res.reason)
    data = res.read()
    print(data)

    httpd.shutdown()
