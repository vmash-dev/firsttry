books = ["Математика", "Фізика", "Хімія", "Фізкультура"]
# total_sum = 0
# for string_number in user_input_as_list:
#     number = float(string_number)
#     # total_sum = total_sum + number
#     total_sum += number
#     print(total_sum, "-------")
total_sum = 0
fiz_books = []
for book in books:
    total_sum += 1
    if book.startswith("Фіз"):
        print(1111111111)
        fiz_books.append(book)

print(total_sum)
print(fiz_books)