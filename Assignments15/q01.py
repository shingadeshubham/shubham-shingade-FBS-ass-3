class Book:
    
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object created")


    def __del__(self):
        print(f"Book object with id {self.bid} destroyed")

    
    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        print("-------------------------")


b1 = Book(101, "shubham", 500, "John Doe")
b2=Book(102,"vijay",200,"mauli")
 
b1.showBook()
b2.showBook()
