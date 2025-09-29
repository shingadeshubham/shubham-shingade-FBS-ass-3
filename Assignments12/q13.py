s = "Python123"
digits = 0
letters = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print("Digits:", digits)
print("Letters:", letters)
