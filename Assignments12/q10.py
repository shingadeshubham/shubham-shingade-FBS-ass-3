s1 = "hello"
s2 = "worldwide"


count1, count2 = 0, 0
for _ in s1:
    count1 += 1
for _ in s2:
    count2 += 1

if count1 > count2:
    print("Larger String:", s1)
else:
    print("Larger String:", s2)
