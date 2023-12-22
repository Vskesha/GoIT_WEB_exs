from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(data)
        self.send_response(201)
        self.end_headers()
        self.wfile.write(b'Done request! ' + data)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<h1>Hello, world!</h1>')


def run_server(server_class=HTTPServer, handler_class=MyHTTPHandler):
    address = ('localhost', 5000)
    http_server = server_class(address, handler_class)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


if __name__ == '__main__':
    run_server()
