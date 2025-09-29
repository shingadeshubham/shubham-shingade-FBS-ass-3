list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
union = []

for i in list1:
    if i not in union:
        union.append(i)
for j in list2:
    if j not in union:
        union.append(j)

print("Union:", union)
