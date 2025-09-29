list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = []

for i in list1:
    if i in list2 and i not in intersection:
        intersection.append(i)

print("Intersection:", intersection)
