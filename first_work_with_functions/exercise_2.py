from first_work_with_functions.exercise_1 import get_greeting, multiply_numbers

def main():
    username = get_greeting("Vanya")
    print(username)
    result = multiply_numbers(number1=4, number2=5)
    print("Площа прямокутника(S = a * b) --")
    print(result)

main()