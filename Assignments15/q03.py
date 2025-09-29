class Shirt:
    
    def __init__(self, sid=None, sname=None, type_=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type_ = type_
        self.price = price
        self.size = size
        print("Shirt object created")

    
    def __del__(self):
        print(f"Shirt object with id {self.sid} destroyed")

    
    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type_)
        print("Price:", self.price)
        print("Size:", self.size)
        print("-------------------------")

s1 = Shirt(301, "Formal Shirt", "Formal", 1200, "Medium")
s2 = Shirt()
s1.showShirt()
s2.showShirt()
