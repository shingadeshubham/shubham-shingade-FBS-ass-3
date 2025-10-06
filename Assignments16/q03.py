class Shirt:
    size_price_increase = {"Small": 0, "Medium": 0.1, "Large": 0.2, "X-Large": 0.3}  # Static concept

    def __init__(self, sid=None, sname=None, type_=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type_ = type_
        self.price = price
        self.size = size
        self.applySizePrice()
        print("Shirt object created")

    def __del__(self):
        print(f"Shirt object with id {self.sid} destroyed")

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type_)
        print("Size:", self.size)
        print("Price:", self.price)
        print("-------------------------")

    
    def applySizePrice(self):
        if self.size in Shirt.size_price_increase and self.price is not None:
            self.price = self.price * (1 + Shirt.size_price_increase[self.size])


s1 = Shirt(301, "Formal Shirt", "Formal", 1000, "Medium")
s2 = Shirt(302, "Casual Shirt", "Casual", 1000, "Large")
s1.showShirt()
s2.showShirt()
