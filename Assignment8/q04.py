def sumofodd(n):
    total=0
    for i in range(1,n+1,2):
        total+=i
    return total
n=int(input("enter the we want to print the odd number which we want:"))
print("sum of odd number between 1 to",n,"is",sumofodd(n))
