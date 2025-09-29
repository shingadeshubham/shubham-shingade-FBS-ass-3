numbers = [10, 21, 4, 45, 66, 93, 11]
even = []
odd = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even List:", even)
print("Odd List:", odd)
