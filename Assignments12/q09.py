s = "Python is great"
char_count = 0
word_count = 1  # at least one word if not empty

for ch in s:
    char_count += 1
    if ch == " ":
        word_count += 1

print("Characters:", char_count)
print("Words:", word_count)
