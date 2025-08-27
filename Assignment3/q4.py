side1=int(input('enter your triangle side1:'))
side2=int(input('enter your triangle side2:'))
side3=int(input('enter your triangle side3:'))
if(side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2):
    print("it is  valid trianle")
else:
    print("it is not valid triangle")