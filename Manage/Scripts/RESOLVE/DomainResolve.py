import urllib2
import json
import sys
import socket
class Resolve():
    def __init__(self,url):
        self.url = str(url).replace("https://","").replace("http://","").replace("http://","").replace("/","")
        print self.url
	
    def Get(self):
        return socket.gethostbyname(self.url)        


