# class Person:
#     _count=0
#     def __init__(self,name):
#         self.name=name
#         Person._count+=1
    
#     @classmethod
#     def getcount(cls):
#         return cls._count
# p1 = Person("John")
# p2= Person("Jimmy")

# print(Person.getcount())

class Temparature:

    def __init__(self,celsius):
        self.celsius=celsius
    
    @classmethod
    def from_farenheit(cls,farenheit):
        celsius = (farenheit -32) *5/9
        return cls(celsius)

temp = Temparature.from_farenheit(98.6)
print(temp.celsius)