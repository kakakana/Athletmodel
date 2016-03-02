
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

port = 8868

httpd = HTTPServer(('', port), BaseHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

