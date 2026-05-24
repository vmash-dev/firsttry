class Calculator:
    name_of_file = "log222.csv"
    def __init__(self):
        self.count = 0

    def set_counter(self):
        self.count += 1

    def log(self, name_of_method, argument_1, argument_2, result):
        with open(file=self.name_of_file, mode='a') as file:
            file.write(f'{name_of_method};{argument_1};{argument_2};{result}\n')
        return

    def add(self, number1, number2):
        answer = number1 + number2
        self.log("add", number1, number2, answer)
        self.set_counter()
        return answer


    def subtraction(self, number3, number4):
        answer_with_subtraction = number3 - number4
        self.log("subtraction", number3, number4, answer_with_subtraction)
        self.set_counter()
        return answer_with_subtraction

    def divion(self, number5, number6):
        self.set_counter()
        if number6 == 0:
            print("На 0 ділити не можна")
            return
        answer_with_division = number5 / number6
        self.log("division", number5, number6, answer_with_division)
        return answer_with_division

    def multiplicator(self, number7, number8):
        answer_with_multiplicator = number7 * number8
        self.set_counter()
        self.log("multiplicator", number7, number8, answer_with_multiplicator)
        return answer_with_multiplicator


calculator = Calculator()
print(calculator.count)
answer = calculator.add(number1=6, number2=7)
answer = calculator.add(number1=2, number2=3)
answer_with_subtraction = calculator.subtraction(number3=12, number4=10)
answer_with_division = calculator.divion(number5=12, number6=10)
answer_with_division = calculator.divion(number5=12, number6=0)

print(answer)
print(answer_with_subtraction)
print(answer_with_division)
print(calculator.count)
