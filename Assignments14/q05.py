strings = ["flower", "flow", "flight"]

if not strings:
    prefix = ""
else:
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]

print("Longest common prefix:", prefix)
