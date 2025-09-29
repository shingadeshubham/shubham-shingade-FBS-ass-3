from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = defaultdict(list)

for word in words:
    sorted_word = "".join(sorted(word))
    anagrams[sorted_word].append(word)

print("Grouped Anagrams:", list(anagrams.values()))
