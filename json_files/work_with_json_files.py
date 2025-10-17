import json

person  = {"first_name": "Іван", "last_name": "Мащенко", "age": 13, "skills": ["Python", "HTML", "Communication"], "has_pet": True, "pet_name": "Tom"}

dict_to_sting = json.dumps(person, ensure_ascii=False, indent=4)
print(dict_to_sting)

with open("person.json", mode='w', encoding="utf-8") as target_file:
    json.dump(person, target_file)

with open("person.json", mode='r', encoding="utf-8") as target_file:
    content = json.load(target_file)
print(content)

content["hobby"] = "chess"
with open("person.json", mode='w', encoding="utf-8") as target_file:
    json.dump(content, target_file)
