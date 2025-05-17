class Book:
    def __init__(self,title,author="Unknown"):
        self.title = title
        self.author = author
    def describe(self):
        return f"The tittle is {self.title} and written by {self.author}"
    
a1 = Book("1984","George")
a2 = Book("Unknown")
print(a1.describe())
print(a2.describe())