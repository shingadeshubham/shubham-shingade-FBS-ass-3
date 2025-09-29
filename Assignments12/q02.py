s = "hello"
n = 2
new_str = ""
for i in range(len(s)):
    if i != n:
        new_str += s[i]
print("After removing:", new_str)
