n = int(input("Enter the number: "))
fact = 1
total = 0

for i in range(1, n+1):
    fact = fact * i
    total = total + i / fact

print("Sum of series:", total)
