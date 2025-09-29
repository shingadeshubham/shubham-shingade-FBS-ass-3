strings = ["apple banana apple", "banana orange", "apple orange banana"]
words = " ".join(strings).split()
unique_words = set(words)
freq = {}

for word in unique_words:
    freq[word] = words.count(word)

print("Unique words:", unique_words)
print("Frequency:", freq)
