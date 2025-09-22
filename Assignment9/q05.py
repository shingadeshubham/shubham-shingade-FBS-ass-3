#Write a program to find factorial using recursion.
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

n=int(input("enter the factorial number which we want:"))
print(fact(n))
    