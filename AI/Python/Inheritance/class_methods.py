#Class Methods
class laptop:
    chargerType = "C-Type"
    def __init__(self,brand):
        self.brand=brand
        self.price=34
    def getPrice(self):
        print(self.price)
    #Instancemethod
    def setPrice(self,price):
        self.price=price
    #Classmethod
    @classmethod
    def changeChargertype(cls):
        cls.chargerType = "B-Type"
        print("Charger Type: ",cls.chargerType)
    #Staticmethod
    @staticmethod
    def info():
        print("This is static method")
    
samsung = laptop("Samsung")
samsung.setPrice(20000)
samsung.getPrice()
samsung.changeChargertype()
samsung.info()