rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    num = i
    for j in range(1, i+1):
        print(num, end="")
        num += 1
    num -= 2
    for j in range(1, i):
        print(num, end="")
        num -= 1
    print()
