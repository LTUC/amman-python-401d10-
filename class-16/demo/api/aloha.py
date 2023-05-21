from http.server import BaseHTTPRequestHandler
from urllib import parse
import platform
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        name = dic.get("name")
        
        
        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stanger"

        message += f"\nGreetings from python version {platform.python_version()}"
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return