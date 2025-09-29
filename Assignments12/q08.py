s = "python"
new_str = ""
for i in range(len(s)):
    if i % 2 == 0:
        new_str += s[i]
print("Modified:", new_str)
