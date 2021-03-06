import requests
import json
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
import webbrowser
import sys
import os
import re

def getCredentials():
    scope = ['https://www.googleapis.com/auth/blogger']
    flow = flow_from_clientsecrets(
        'secrets.json', scope,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    storage = Storage('credentials.dat')
    credentials = storage.get()
    if not credentials or credentials.invalid:
        auth_uri = flow.step1_get_authorize_url()
        webbrowser.open(auth_uri)
        auth_code = input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)
    return credentials

credentials = getCredentials()
blogID='859763561203371182'
APIKEY='AIzaSyDSGVjPMLb0QXm76AMWr8S-f3I6B2keqBc'
if blogID==None:
    blogID=raw_input('enter a blogID: ')
if APIKEY==None:
    APIKEY=raw_input('enter your APIKEY: ')
GET="https://www.googleapis.com/blogger/v3/blogs/"+blogID+"/posts?key="+APIKEY
url="https://www.googleapis.com/blogger/v3/blogs/"+blogID+"/posts/"
headers = {
    'Authorization': APIKEY,
    'Content-Type' : 'application/json'
}

class post:
    def __init__(self, a, args):
        self.JSON = {
            "kind": "blogger#post",
            "blog": { "id": blogID },
            "title": "DEFAULT",
            "content": "<h1>test</h1>"
        }
        self.blogTitles = self.GET(a, 'title')
        self.getLinks   = self.GET(a, 'id')
        self.content    = self.GET(a, 'content')
        self.isPost     = len(args) > 1
        self.validPosts = args if self.isPost else self._getLocalPosts_() 
        self.display()

    def _getLocalPosts_(self):
        return [f for f in os.listdir() if "txt" in f]
        
    def GET(self,st,value):
        if st.status_code is 200:
            val = [None] * len(st.json().get('items'))
            for i in range(0, len(val)):
                val[i] = st.json().get('items')[i].get(value)
            return val
        else:
            return None

    def display(self):
        print("Download a Post")
        numPosts = len(self.blogTitles)
        for i in range(0, numPosts):
            print(str(i)+" : "+self.blogTitles[i])
        print("\nOr Upload an Edit")
        for i in range(numPosts, len(self.validPosts)+numPosts):
            print(str(i)+" : "+self.validPosts[i-numPosts])
        value = input("\nSelect a post: ")
        self.printContent(int(value))
        if (self.isPost):            
            self.POST()
        else:
            self.savePost(int(value))

    def printContent(self, selection):
        os.system('clear')
        print(self.blogTitles[selection]+"\n")
#        print(self.content[selection].replace("<br />","\n").replace(r"<[a-zA-Z0-9/]*>",""))
        print(re.sub(r'<[a-zA-Z-0-9/]*>',' ',self.content[selection].replace("<br />","\n")))

    def printPosts(self):
        for i in range(0, len(self.blogTitles)):
            print(self.blogTitles[i]+": "+self.getLinks[i])

    def savePost(self, post):
        try :
            with open(self.blogTitles[post].replace(" ","")+".txt", "w+") as f:
                f.write(self.content[post].replace("<br />", " "))
            print("Saved")
        except:
            print("Error")

    def POST(self, Title="post", Content="this is a test"):
        self.JSON['title']   = Title
        self.JSON['content'] = Content
        try :
            r = requests.post(url, headers=headers, data=json.dumps(self.JSON))
            if r.status_code is not 200:
                print(r.reason)
                print(r.status_code)
            else :
                print("SUCCESS!")
        except:
            print("error on POST")

st=requests.get(GET)
t = post(st, sys.argv)
