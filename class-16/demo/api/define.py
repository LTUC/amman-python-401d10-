from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        word = dic.get("word")

        if word:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            res = requests.get(url+word)
            data = res.json()
            result = data[0]["meanings"][0]["definitions"][0]["definition"]
        
       
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return