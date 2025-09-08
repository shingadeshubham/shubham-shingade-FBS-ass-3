x = int(input("Enter x: "))
n = int(input("Enter n terms: "))
s = 0
sign = 1
d = 1
for i in range(1, n+1):
    s += sign * (x**i)/d
    sign *= -1
    d += 2
print(s)
