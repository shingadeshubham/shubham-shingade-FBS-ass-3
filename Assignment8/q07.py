def sum_of_digits(num):
    total = 0
    for d in str(num):
        total += int(d)
    return total


num = int(input("Enter a number: "))
print("Sum of digits =", sum_of_digits(num))
