class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype

    def drive(self):
        print('The person drives the car')

    
car = Car(4, 5, 'Diesel')
car.drive()


class audi(Car):
    def __init__(self, windows, doors, enginetype, enableai):
        super().__init__(windows, doors, enginetype)
        self.enableai = enableai

    def selfdriving(self):
        print('Audi supports self driving cars')

new_car = audi(5, 5, 'dielsel', True)
new_car.drive()
new_car.selfdriving()