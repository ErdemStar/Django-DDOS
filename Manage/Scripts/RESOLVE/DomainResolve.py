import urllib2
import json

class Resolve():
    def __init__(self,url):
        if "//" in url:
            self.url = str(url).split("//")[1]
        else:
            self.url = url

    def Get(self):
        resp = urllib2.urlopen(" https://dns-api.org/A/"+self.url).read()
        get = json.loads(resp)
        for i in get:
            if i["type"] == "A":
                return i["value"]
