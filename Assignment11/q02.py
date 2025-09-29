list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged = list1 + list2

#use in that bubble sort
for i in range(len(merged)):
    for j in range(len(merged)-i-1):
        if merged[j] > merged[j+1]:
            merged[j], merged[j+1] = merged[j+1], merged[j]

print("Merged & Sorted List:", merged)
