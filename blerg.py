import requests
import json
import unicodedata

blogID='859763561203371182'
APIKEY='AIzaSyA1XLg6-JAcN1G0NtfcG66QZgasLT0CAJk'

if blogID==None:
    blogID=raw_input('enter a blogID: ')
if APIKEY==None:
    APIKEY=raw_input('enter your APIKEY: ')
GET="https://www.googleapis.com/blogger/v3/blogs/"+blogID+"/posts?key="+APIKEY
PUSH="https://www.googleapis.com/blogger/v3/blogs/"+blogID+"/posts/"
st=requests.get(GET)

class blerg:
    def __init__(self,a):
        self.blogTitles = self.getNames(a)
        self.getLinks   = self.getLinks(self.blogTitles)
        self.content = self.getContent(a)
        self.printContent(1)

    def getNames(self,st):
        if st.status_code is 200:
            val = [None] * len(st.json().get('items'))
            for i in range(0, len(val)):
                val[i] =st.json().get('items')[i].get('title')
            return val
        else:
            return None

    def getLinks(self,titles):
        if st.status_code is not 200:
            return None
        else:
            val = [None] * len(st.json().get('items'))
            for i in range(0, len(val)):
                val[i] = st.json().get('items')[1].get('id')
            return val

    def getContent(self, st):
        if st.status_code is not 200:
            return None
        else:
            #init array of items
            val = [None] * len(st.json().get('items'))
            for i in range(0, len(val)):
                val[i] = st.json().get('items')[1].get('content')
            return val

    def printContent(self, selection):
        print(self.content[selection])

    def printPosts(self):
        for i in range(0, len(self.blogTitles)):
            print(self.blogTitles[i]+": "+self.getLinks[i])

    def POST(self, file):
        #post a blog
        requests.post()

blerg(st)
