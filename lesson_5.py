list_of_travel = ["Одеса", "Київ", "Харків", "Кривий Ріг", "Запоріжжя"]
friends_list = ["Житомир", "Вінниця"]
list_of_travel.extend(friends_list)
print(list_of_travel)
fifth_city = list_of_travel[4]
list_of_travel.remove(fifth_city)
print(list_of_travel)
list_of_travel.sort()
print(list_of_travel)
# print(is_user_input_digit)
# if is_user_input_digit:
#     print('Дякую, ви ввели число')
#     print('Дякую, ви ввели число')
#     print('Дякую, ви ввели число')
# else:
#     print("Not a number")
for city in list_of_travel:
    if city.startswith("К"):
        print(city, "Тут треба зробити фото")
    else:
        print(city)
new_city = "Черкаси"
list_of_travel.insert(1, new_city)
print(list_of_travel)

total_sum_of_city = 0
for city in list_of_travel:
    total_sum_of_city = total_sum_of_city + 1

# total_sum = 0
# for string_number in user_input_as_list:
#     number = float(string_number)
#     # total_sum = total_sum + number
#     total_sum += number
#     print(total_sum, "-------")
print(total_sum_of_city)