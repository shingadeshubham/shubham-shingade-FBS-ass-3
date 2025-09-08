p = int(input("Enter number of passengers: "))
cost = int(input("Enter cost per ticket: "))
total = 0

for i in range(p):
    age = int(input("Enter age: "))
    if age < 12:
        total += cost * 0.7
    elif age > 59:
        total += cost * 0.5
    else:
        total += cost

print("Total Cost =", total)
