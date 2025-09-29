dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Method without using update()
merged = {}
for k, v in dict1.items():
    merged[k] = v
for k, v in dict2.items():
    merged[k] = v

print("Concatenated Dictionary:", merged)
