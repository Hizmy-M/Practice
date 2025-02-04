class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def display_info(self):
        print(f'{self.__name}')


person_one = Person('asd', 'asd')
person_one.display_info()

