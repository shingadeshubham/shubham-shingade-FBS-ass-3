s = "this is a test this is"
words = s.split()
occurrences = {}

for w in words:
    if w in occurrences:
        occurrences[w] += 1
    else:
        occurrences[w] = 1

print("Word Count:", occurrences)
