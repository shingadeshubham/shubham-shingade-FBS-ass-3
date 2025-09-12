def is_armstrong(num):
    order = len(str(num))
    total = 0
    for d in str(num):
        total += int(d) ** order
    return total == num


num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")
