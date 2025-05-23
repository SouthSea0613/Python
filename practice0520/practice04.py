from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response_only(200, 'OK')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print('Started httpserver on port 8888')
    print('Press Ctrl+C to quit')
    server.serve_forever()