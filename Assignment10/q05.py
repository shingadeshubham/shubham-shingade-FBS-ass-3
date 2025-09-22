lst = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter a number: "))

count = 0
for i in lst:
    if i == num:
        count += 1

if count > 0:
    print(num, "is present", count, "times")
else:
    print(num, "is not present")
