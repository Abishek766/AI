class Person:
    #Fields(Variables)
    drink=""
    #Constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #Method
    def greet(self):
        print(f"Hello! I am {self.name} and my age is {self.age}")
person1=Person("Abishek",23)
person1.drink="No"
print(person1.drink)
person1.greet()