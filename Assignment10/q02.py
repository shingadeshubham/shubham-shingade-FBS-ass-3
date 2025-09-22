lst = [7, 3, 9, 1, 6]
max_val = lst[0]
min_val = lst[0]

for i in lst:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum:", max_val)
print("Minimum:", min_val)
