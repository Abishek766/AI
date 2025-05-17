#Inheritance
# Single Inheritance
# class Animal:
#     def speak(self):
#         print("Animal can speak")

# class Dog(Animal):
#     def speaks(self):
#         print("Dog can speak")

# D=Dog()
# D.speaks()
# D.speak()

# Muliple Inheritance
# class A:
#     def display(self):
#         print("This is Parent Class")
# class B:
#     def display(self):
#         print("This is another parent class")
# class C(B , A):
#     pass
# c1 = C()
# c1.display() # This calls B parent class because it follows MRO rule(Method Resolution Order)

# Multilevel Inheritance
# class GrandFather:
#     def display(self):
#         print("I am a first generation person in this family")
# class Father(GrandFather):
#     def show(self):
#         print("I am a second generation persin in this family")
# class Child(Father):
#     def speak(self):
#         print("Hi..!, I am a current generation person in this family")
# c = Child()
# c.speak()
# c.show()
# c.display()

#Hierarchical Inheritance

# class Parent:
#     def display(self):
#         print("Hello, I am Parent")
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# c1=Child1()
# c1.display()
# c2=Child2()
# c2.display()

#Hybrid Inheritance
# class A:
#     pass

# class B(A):
#     def display(self):
#         print("I am the parent")

# class C:
#     pass

# class D(B, C):  # Combines multiple + multilevel
#     pass

# d = D()
# d.display()

# Issubclass method() & Isintance method()
# class Calculation1:
#     def summation(self,a,b):
#         return a + b
# class Calculation2:
#     def multiply(self,a,b):
#         return a * b
# class Derived(Calculation1 , Calculation2):
#     def divide(self,a,b):
#         return a/b
# d = Derived()
# print(issubclass(Derived,Calculation1))
# print(issubclass(Derived,Calculation2))
# print(issubclass(Calculation1,Calculation2))
# print(isinstance(d,Derived))

#Super Keyword
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B")
class C(B, A):
    def __init__(self):
        super().__init__()
        print("C")
obj = C()

