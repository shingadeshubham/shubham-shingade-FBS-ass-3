list1 = [[1, 2], [4, 1], [9, 5], [3, 0]]

for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if list1[j][1] > list1[j+1][1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("Sorted by second element:", list1)
