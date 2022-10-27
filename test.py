# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

import json
import requests

#keyword = input("Enter keyword: ")

request = "https://api.tvmaze.com/search/shows?q=girls"
#request = "https://api.tvmaze.com/search/shows?q=" 

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")

