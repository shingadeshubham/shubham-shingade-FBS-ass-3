class Product:
    
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    
    def __del__(self):
        print(f"Product object with id {self.pid} destroyed")


    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("-------------------------")


p1 = Product(201, "Laptop", 50000, 2)
p2 = Product()
p1.showProduct()
p2.showProduct()
