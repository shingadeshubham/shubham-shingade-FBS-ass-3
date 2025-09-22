# Program to remove even numbers from list

lst = [10, 15, 20, 25, 30, 35, 40]
new_list = []

for i in lst:
    if i % 2 != 0:     #  only odd numbers
        new_list.append(i)

print("List after removing even numbers:", new_list)
