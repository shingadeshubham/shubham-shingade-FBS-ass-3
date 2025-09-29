words = ["python", "is", "fun", "awesome"]

for i in range(len(words)):
    for j in range(len(words)-i-1):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]

print("Sorted by length:", words)
