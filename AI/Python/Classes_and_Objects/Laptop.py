class Laptop:
    Price=0
    Processor=""
    RAM = ""
    def __init__(self, Price,Processor,RAM):
        self.Price=Price
        self.Processor=Processor
        self.RAM=RAM
    def details(self):
        print(f"The laptop contains {self.Price},the processor is {self.Processor} and the ram is {self.RAM}")

Dell = Laptop(50000,"Intel core 9","16 GB")
HP = Laptop(60000,"Intel Core 7","8 GB")
Lenovo = Laptop(45000,"Intel Core 5","16 GB")

Dell.details()
HP.details()
Lenovo.details()