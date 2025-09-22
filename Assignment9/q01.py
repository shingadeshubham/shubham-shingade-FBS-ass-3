#Write a program to find sum of following series using recursive functions:

#i. 1! + 2! + 3! + 4! +..... + n!
def factorial(n):
    if n==0 or n==1: 
        return 1
    return n * factorial(n-1)

def sum_factorial(n):
    if n==0:
        return 0
    return factorial(n) + sum_factorial(n-1)

n=int(input("enter the number:"))
print("sum of series",sum_factorial(n))
