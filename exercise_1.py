from pprint import pprint

import requests

url = "https://gutendex.com/books"
params = {

}

response = requests.get(url, params=params)

print(response)

response_json = response.json()

results = response_json["results"]

for book in results:
    name_of_book = book['title']
    authors = book['authors']
    if authors:
        first_autor = authors[0]
        birth_of_autor = first_autor['birth_year']
        if name_of_book == "A Room with a View":
            print(birth_of_autor)



