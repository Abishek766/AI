#Constructor and bulit in class functions

# class Student:
#     def __init__(self):
#         print("The First Constructor")
#     def __init__(self):
#         print("The Second Constructor") # The constructor call the last constructor 
# s1=Student()

# bulit in function

class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
s1=Student("John",101,23)

# print(getattr(s1,"name"))

setattr(s1,"age",24)
# print(getattr(s1,"age"))

print(hasattr(s1,"id"))

delattr(s1,"age")
print(s1.age)