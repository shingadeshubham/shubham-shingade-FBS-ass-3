num = int (input("enter your three digit number :"))
d1= num // 100 #4

d2= (num //10)%10 #2

d3=num % 10 #8

if(d1==(d2 *2)and d3==(d1*2)):
    print("yes you have done it")
else:
    print("please try next time")
