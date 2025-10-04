from pprint import pprint

import requests

url = "http://api.open-notify.org/astros.json"
params = {
    "limit": 1000,
    "skip": 0
}

response = requests.get(url, params=params)

print(response)

response_json = response.json()
#pprint(response_json)

people = response_json["people"]
#pprint(people)

list_people_on_ISS = []

for human in people:
    #is_female = user["gender"] == "female"
    is_iss = human["craft"] == "ISS"
    if is_iss :
        list_people_on_ISS.append(human["name"])
        print(human["name"])


print(list_people_on_ISS)
