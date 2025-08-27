side1=int(input("enter the length of side 1: "))
side2=int(input("enter the length of side 2: "))
side3=int(input("enter the length of side 3:"))
if(side1==side2 ==side3 ):
    print("it is equalilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("it is isosceles triangle ")
else:
    print("it is scalene triangle")