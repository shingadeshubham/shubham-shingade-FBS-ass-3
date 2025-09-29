numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

for n in numbers:
    if n % 2 != 0:
        result.append(n)

print("List after removing even numbers:", result)
