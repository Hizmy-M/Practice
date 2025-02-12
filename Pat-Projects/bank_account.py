class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 


    def display(self):
        return f"Name: {self.name} age {self.age}"
    

person_one = Person('Test', 123)
print(person_one.display())