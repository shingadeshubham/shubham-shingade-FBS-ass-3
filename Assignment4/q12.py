start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    power = len(str(num))
    s = 0
    temp = num
    while temp > 0:
        d = temp % 10
        s += d**power
        temp //= 10
    if s == num:
        print(num, end=" ")
