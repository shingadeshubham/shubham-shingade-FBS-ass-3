# Program to find larger string without using built-in functions

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")


count1, count2 = 0, 0

for _ in s1:
    count1 += 1
for _ in s2:
    count2 += 1

# Compare
if count1 > count2:
    print("Larger String:", s1)
elif count2 > count1:
    print("Larger String:", s2)
else:
    print("Both strings are of equal length")
