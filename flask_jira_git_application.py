from flask import Flask #From flask package, import Flask module(Collection of functions)
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__) #Create a flask application instance

@app.route('/createJira', methods=['POST']) # decorator, makes sure that before invoking an function, perform the action in app.route
def createJira():
  url = "https://shyamsaisatishedu.atlassian.net/rest/api/3/issue"

  auth = HTTPBasicAuth("shyamsaisatish.edu@gmail.com", "<api-token>")

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
  }

  payload = json.dumps( {
    "fields": {
      "description": {
        "content": [
          {
            "content": [
              {
                "text": "Create First Jira ticket",
                "type": "text"
              }
            ],
            "type": "paragraph"
          }
        ],
        "type": "doc",
        "version": 1
      },
      "project": {
        "key": "GJI"  #Here by default, it was id instead of key
      },
      "issuetype": {
        "id": "10007" 
      },
      "summary": "Creating First Jira ticket using Python",
    },
    "update": {}
  } )

  response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    ) 

  return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# if __name__ == '__main__':
# app.run("0.0.0.0") -> will run on port 5000 by default
app.run('0.0.0.0',port=6000)