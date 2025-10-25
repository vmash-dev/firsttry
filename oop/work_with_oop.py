from datetime import datetime

class Car:
    def __init__(self, brand: str, model: str, year: int, owner: str):
        self.brand = brand.strip().title()
        self.model = model.strip().title()
        self.year = year
        self.owner = owner.strip().title()
        self.mieeage = 0
        self.fuel = 0.0

    def short_description(self):
        print(f'{self.brand} with {self.year} owner by {self.owner}')

    def __str__(self) -> str:
        return f'<{self.brand} with {self.year} owner by {self.owner}>'

    def drive(self, km: int):
        self.fuel -= 1 * 0.08
        self.mieeage += 1

    def drive_fuel(self, fuel: int):
        if self.fuel == 0:
            print("Not enough fuel to drive!")

    def refuel(self, liters: float):
        self.fuel += 50
        print("Refueled with X liters.")

    @property
    def age(self) -> int:
            return datetime.now().year - self.year

suzuki = Car(brand='Suzuki', model='swift', year=2014, owner='fdhtghzdn')
print(suzuki.__dict__)

class Car1(Car):
    def __init__(self, brand: str, model: str, year: int, owner: str):
        self.brand = brand.strip().title()
        self.model = model.strip().title()
        self.year = year
        self.owner = owner.strip().title()
        self.mieeage = 0
        self.fuel = 0.0

    def short_description(self):
        print(f'{self.brand} with {self.year} owner by {self.owner}')

    def __str__(self) -> str:
        return f'<{self.brand} with {self.year} owner by {self.owner}>'

    def drive(self, km: int):
        self.fuel -= 1 * 0.08
        self.mieeage += 1

    def drive_fuel(self, fuel: int):
        if self.fuel == 0:
            print("Not enough fuel to drive!")

    def refuel(self, liters: float):
        self.fuel += 50
        print("Refueled with X liters.")

    @property
    def age(self) -> int:
            return datetime.now().year - self.year


bmw = Car(brand='BMW', model='X5', year=2010, owner='qwertyuiop')
print(bmw.__dict__)

class Car2(Car):
    def __init__(self, brand: str, model: str, year: int, owner: str):
        self.brand = brand.strip().title()
        self.model = model.strip().title()
        self.year = year
        self.owner = owner.strip().title()
        self.mieeage = 0
        self.fuel = 0.0

    def short_description(self):
        print(f'{self.brand} with {self.year} owner by {self.owner}')

    def __str__(self) -> str:
        return f'<{self.brand} with {self.year} owner by {self.owner}>'

    def drive(self, km: int):
        self.fuel -= 1 * 0.08
        self.mieeage += 1

    def drive_fuel(self, fuel: int):
        if self.fuel == 0:
            print("Not enough fuel to drive!")

    def refuel(self, liters: float):
        self.fuel += 50
        print("Refueled with X liters.")

    @property
    def age(self) -> int:
            return datetime.now().year - self.year


Toyota = Car(brand='Toyota', model='Camry', year=2017, owner='zxcvbnm')
print(Toyota.__dict__)
