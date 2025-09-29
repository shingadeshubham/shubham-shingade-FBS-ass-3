s = "python is fun"
new_str = ""
for ch in s:
    if ch == " ":
        new_str += "-"
    else:
        new_str += ch
print("Modified:", new_str)
