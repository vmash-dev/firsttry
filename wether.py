from pprint import pprint

import requests

url = "http://api.weatherstack.com/current"
params = {
    "access_key": "e145d039aad3ed9d8355850807c53211",
    "query": "london"
}
#posts = response_json['posts']
#pprint(posts)

#for post in posts:
  #reactions = post["reactions"]
  #if reactions['likes'] >= 800:
    #print(post)
response = requests.get(url, params=params)

print(response.url)

response_json = response.json()

#pprint(response_json)

city_temperature = response_json['current']
print(city_temperature)
temperature = city_temperature["temperature"]
print(temperature)