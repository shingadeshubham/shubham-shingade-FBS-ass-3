numbers = [1, 3, -5, 4, -2, 6]
max_product = float('-inf')
pair = ()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        product = numbers[i] * numbers[j]
        if product > max_product:
            max_product = product
            pair = (numbers[i], numbers[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_product)
