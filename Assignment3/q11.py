total = 0
for i in range(5):
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket price: "))
    if age < 12:
        total += ticket * 0.7
    elif age > 59:
        total += ticket * 0.5
    else:
        total += ticket
print("Total ticket amount:", total)
