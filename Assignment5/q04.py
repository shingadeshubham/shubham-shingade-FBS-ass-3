num = int(input("Enter number: "))
s = str(num)
power = len(s)
total = 0

for d in s:
    total += int(d) ** power

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")
