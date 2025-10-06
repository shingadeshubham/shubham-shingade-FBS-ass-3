class Product:
    discount = 0.1  # 10% discount as static member

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

    
    def applyDiscount(self):
        if self.price is not None:
            self.price = self.price * (1 - Product.discount)
        return self.price


p1 = Product(201, "Laptop", 50000, 2)
p1.showProduct()
p1.applyDiscount()
print("Price after discount:", p1.price)
