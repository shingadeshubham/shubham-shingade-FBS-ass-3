cp = int(input("enter the cost price:"))
sp = int(input("enter the selling price:"))
if sp > cp:
    print("profit") 
elif cp > sp :
    print("loss")
else:
    print(" no profit no loss")
