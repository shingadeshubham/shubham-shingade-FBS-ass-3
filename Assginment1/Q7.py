import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots are real:", r1, r2)
elif d == 0:
    r = -b / (2*a)
    print("Roots are equal:", r)
else:
    print("Roots are imaginary")
