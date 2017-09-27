'''
Implement a basic http server using python, based on the computer science 50 at Hardvard University.
'''
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        Resolves the get method,function overwrite
        '''
        # send response status code
        self.send_response(200)

        # send headers
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Hallo World", "utf-8"))

# server configurations
port = 8080
server_address =('0.0.0.0', port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

#run my http servercito
print('Listening')
httpd.serve_forever()
