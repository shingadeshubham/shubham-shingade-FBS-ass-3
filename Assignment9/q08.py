#Write a program to check whether a number is prime or not using recursion.
#
def prime(n,i=2):
    if n<=1:
        return False
    if i*i >n:
        return True
    if n% i==0:
        return False
    return prime(n,i+1)
n=int(input("enter the number:"))
print(prime(n))
