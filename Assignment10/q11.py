lst = [10, 20, 30, 40, 50, 60]
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in lst:
    if i % m == 0 and i % n == 0:
        print(i, end=" ")
