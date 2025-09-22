lst = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter element to remove: "))
new_lst = []

for i in lst:
    if i != num:
        new_lst.append(i)

print("List after removing", num, ":", new_lst)
