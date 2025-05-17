#Class Varaible vs Instance Varaible
# class Dog:
#     species = "Carines Families"

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# dog1 = Dog("Jimmy",5)
# dog2 = Dog("Subramani",3)

# print(dog2.name)
# print(dog1.age)
# print(dog1.species)

#Modify Class Variable

class Car:
    wheel = 4

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

car1 = Car("Toyato","SUV")
car2 = Car("Audi","Accord")

car1.wheel=3
print(car1.wheel)
print(car2.wheel)
print(Car.wheel)