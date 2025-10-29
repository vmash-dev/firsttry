class Animal:
    def __init__(self, name: str):
        self.name = name.strip()

    def make_sound(self):
        print('Тварина видає звук')

    def info(self):
        print(f'{self.name}')

class Dog(Animal):
    def __str__(self):
        return f"Dog {self.name}"

    def make_sound(self):
        print("Гав")

class Cat(Animal):
    def __str__(self):
        return f"Cat {self.name}"

    def make_sound(self):
        print("Мяу")

class Bird(Animal):
    def fly(self):
        print("Птах летить")

bird = Bird(name="Кеша")
bird.fly()

cat = Cat(name= "Мурка")
cat.make_sound()

print(cat)

