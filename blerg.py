import requests
import json
from oauth2client.client import flow_from_clientsecrets
blogID='859763561203371182'
APIKEY='AIzaSyDSGVjPMLb0QXm76AMWr8S-f3I6B2keqBc'

flow = flow_from_clientsecrets('secrets.json',
                               scope='https://www.googleapis.com/auth/blogger',
                               redirect_uri='http://evanpeterjones.com')
#print(dir(flow))
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

class blerg:
    def __init__(self,a):
        self.JSON = {
            "kind": "blogger#post",
            "blog": { "id": blogID },
            "title": "DEFAULT",
            "content": "<h1>test</h1>"
        }
        self.blogTitles = self.GET(a, 'title')
        self.getLinks   = self.GET(a, 'id')
        self.content    = self.GET(a, 'content')
        print("Select a Post")
        for i in range(0, len(self.blogTitles)):
            print(str(i)+" : "+self.blogTitles[i])
        val=input(" ")
        self.printContent(int(val))
        self.savePost(int(val))
#        self.POST()

    def GET(self,st,value):
        if st.status_code is 200:
            val = [None] * len(st.json().get('items'))
            for i in range(0, len(val)):
                val[i] = st.json().get('items')[i].get(value)
            return val
        else:
            return None

    def printContent(self, selection):
        print(self.content[selection])

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

    #pass me a file i'll make it json and post it
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
blerg(st)
