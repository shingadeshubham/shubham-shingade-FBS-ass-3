lst = [1, 2, 2, 3, 4, 3, 5, 1]
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

print("List after removing duplicates:", unique)
