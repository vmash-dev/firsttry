from pprint import pprint

import requests

url = "https://gutendex.com/books"
params = {

}

response = requests.get(url, params=params)

print(response)

response_json = response.json()

results = response_json["results"]

#pprint(results)
for book in results:
    #print(book)
    name_of_book = book['title']
    #print(name_of_book)
    authors = book['authors']
    #print(authors)
    if authors:
        first_autor = authors[0]
        #print(first_autor)
        birth_of_autor = first_autor['birth_year']
        #print(birth_of_autor)
        if name_of_book == "A Room with a View":
            print(birth_of_autor)

    #print("="*50)

