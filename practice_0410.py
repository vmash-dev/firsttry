from pprint import pprint

import requests

url = "https://restcountries.com/v3.1/translation/ukraine"
params = {
    "limit": 1000,
    "skip": 0
}

response = requests.get(url, params=params)

print(response)


response_json = response.json()
#pprint(response_json)
first_country = response_json[0]
borders = first_country['borders']
print(borders)

