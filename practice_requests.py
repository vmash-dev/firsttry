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

u = {'address': {'address': '626 Main Street',
                 'city': 'Phoenix',
                 'coordinates': {'lat': -77.16213, 'lng': -92.084824},
                 'country': 'United States',
                 'postalCode': '29112',
                 'state': 'Mississippi',
                 'stateCode': 'MS'},
     'age': 28,
     'bank': {'cardExpire': '03/26',
              'cardNumber': '9289760655481815',
              'cardType': 'Elo',
              'currency': 'CNY',
              'iban': 'YPUXISOBI7TTHPK2BR3HAIXL'},
     'birthDate': '1996-5-30',
     'bloodGroup': 'O-',
     'company': {'address': {'address': '263 Tenth Street',
                             'city': 'San Francisco',
                             'coordinates': {'lat': 71.814525, 'lng': -161.150263},
                             'country': 'United States',
                             'postalCode': '37657',
                             'state': 'Wisconsin',
                             'stateCode': 'WI'},
                 'department': 'Engineering',
                 'name': 'Dooley, Kozey and Cronin',
                 'title': 'Sales Manager'},
     'crypto': {'coin': 'Bitcoin',
                'network': 'Ethereum (ERC20)',
                'wallet': '0xb9fc2fe63b2a6c003f1c324c3bfa53259162181a'},
     'ein': '977-175',
     'email': 'emily.johnson@x.dummyjson.com',
     'eyeColor': 'Green',
     'firstName': 'Emily',
     'gender': 'female',
     'hair': {'color': 'Brown', 'type': 'Curly'},
     'height': 193.24,
     'id': 1,
     'image': 'https://dummyjson.com/icon/emilys/128',
     'ip': '42.48.100.32',
     'lastName': 'Johnson',
     'macAddress': '47:fa:41:18:ec:eb',
     'maidenName': 'Smith',
     'password': 'emilyspass',
     'phone': '+81 965-431-3024',
     'role': 'admin',
     'ssn': '900-590-289',
     'university': 'University of Wisconsin--Madison',
     'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 '
                  'Safari/537.36',
     'username': 'emilys',
     'weight': 63.16}
