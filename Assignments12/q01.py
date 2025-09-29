s = "banana"
new_str = ""
for ch in s:
    if ch == 'a':
        new_str += '$'
    else:
        new_str += ch
print("Modified String:", new_str)
