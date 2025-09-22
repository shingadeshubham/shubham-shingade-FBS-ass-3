lst = [10, 21, 4, 45, 66, 93, 11]
even_list = []
odd_list = []

for i in lst:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even List:", even_list)
print("Odd List:", odd_list)
