import json
import requests

#exercise1
print("----------------------exercise1----------------------------------")

response = requests.get("https://api.chucknorris.io/jokes/random").json()
print(response["value"])


#exercise2
print("----------------------exercise2----------------------------------")

city = input("Enter the city: ")
key = "" #paste your key here
request = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key +"&units=metric"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        temperature = int(json_response["main"]["temp"])
        description = json_response["weather"][0]["description"]
        print(f"Current weather in {city.capitalize()} is {temperature}°C with a {description}.")
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")