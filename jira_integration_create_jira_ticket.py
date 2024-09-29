import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shyamsaisatishedu.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("shyamsaisatish.edu@gmail.com", "<api-toke>")

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

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))