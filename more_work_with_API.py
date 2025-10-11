from pprint import pprint

import requests

url = "https://gutendex.com/books/53360/"
params = {

}

response = requests.get(url, params=params)

print(response)

response_json = response.json()
#pprint(response_json)
subjects = response_json['subjects']
#pprint(subjects)
for subject in subjects:
    print(subject)