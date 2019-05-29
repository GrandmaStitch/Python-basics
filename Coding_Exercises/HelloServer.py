#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloServer(BaseHTTPRequestHandler):
	def do_GET(self):
		# return the server version
		server_version = 'HelloServer/1.2'
		
		# a response includes 3 parts: response code, some headers, a response body
		# return a response code
		self.send_response(200)
		
		# return response headers
		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.send_header('user-	defined-content', 'undefined')
		# return the blank line ending the MIME headers.
		self.end_headers()

		# return a response body
		self.wfile.write('Hello, this is a Python server\n\n'.encode())
		self.wfile.write('Now, we try to output the request headers: \n{}\n'.format(self.headers).encode())

		# more useage
		# the request stores in self.raw_requestlin variable; 
		print('This is the requestline, the same as the request: {}'.format(self.requestline))
		print('This is the request: {}'.format(self.raw_requestline))
		print('Return the HTTP verb: {}'.format(self.command))
		print('Return the request path: {}'.format(self.path))
		print('Return the request version: {}'.format(self.request_version))
        # get connection status
		print(self.headers.get('Connection', ""))


def run(server_class=HTTPServer, handler_class=HelloServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
