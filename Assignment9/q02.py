#Write a program to check if given number is Armstrong or not using recursive
#function.

def armstrongnumber(num,power):
    if num==0:
        return 0
    return (num%10) ** power + armstrongnumber(num//10,power)
n=int(input("enter the number:"))
if n== armstrongnumber(n,len(str(n))):
    print("it is a armstrong number",n)
else:
    print("it is not armstrong number",n)    
