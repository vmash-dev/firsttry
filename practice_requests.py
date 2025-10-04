from pprint import pprint

import requests

url = "https://dummyjson.com/posts"
params = {
    "limit": 1000,
    "skip": 0
}

response = requests.get(url, params=params)

print(response)

response_json = response.json()
# pprint(response_json)

posts = response_json['posts']
pprint(posts)

for post in posts:
    reactions = post["reactions"]
    if reactions['likes'] >= 800:
        print(post)
