#exercise1
print("----------------------exercise1----------------------------------")
import json
import requests

#keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.chucknorris.io/jokes/random"

response = requests.get(request)
if response.status_code==200:
    json_response = response.json()
    print(json.dumps(json_response, indent=2))
    for a in json_response:
        print(a["value"])
