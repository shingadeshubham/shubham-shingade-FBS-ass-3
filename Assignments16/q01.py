class Book:
    count=0
    def __init__(self,bid,bname,bprice,bauthor):
        self.bookid=bid
        self.bookname=bname
        self.bookprice=bprice
        self.bookauthor=bauthor

    def  display(self):
        print(f"bookid:: (self.bid)")
        print(f"bookname::(self.bname)")
        print(f"bookprice::(self.bprice)")
        print(f"bookauthor:(self.author)")

    def __del__(self):
        print("destructor is called")

b1=Book(10,"the fly",2000,"shubham")
