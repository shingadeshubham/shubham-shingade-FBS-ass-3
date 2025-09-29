numbers = [12, 35, 1, 10, 34, 1]

# Bubble Sort
for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Second Largest Number:", numbers[-2])
