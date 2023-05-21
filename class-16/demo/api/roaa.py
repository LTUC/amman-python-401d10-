from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        message = "Welcome Roaa ^_^"
        self.wfile.write(message.encode('utf-8'))
        return