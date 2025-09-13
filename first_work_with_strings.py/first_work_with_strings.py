smile = "😉"
user_input = input("ввести 5 імен однокласників, через пробіл: ")
user_input = user_input.strip()
user_input = user_input.title()
user_input = user_input.replace(" ", smile)
cool_friends = "- ви класні друзяки"
sus = ("=")

header = sus * 30

friends = f"{user_input} {cool_friends} "

print(header)

print(friends)

print(header)
