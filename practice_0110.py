from pprint import pprint

import requests

url = "https://dummyjson.com/users"
params = {
    "limit": 1000,
    "skip": 0
}

response = requests.get(url, params=params)

print(response)

response_json = response.json()
# pprint(response_json)

users = response_json['users']

for user in users:
    is_female = user["gender"] == "female"
    is_relevant_age = user["age"] >= 30
    address = user["address"]
    is_it_austin = address["city"] == "Austin"
    if is_female and is_relevant_age and is_it_austin:
        print(user)