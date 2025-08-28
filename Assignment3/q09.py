s1 = int(input("Enter mark of subject 1: "))
s2 = int(input("Enter mark of subject 2: "))
s3 = int(input("Enter mark of subject 3: "))
s4 = int(input("Enter mark of subject 4: "))
s5 = int(input("Enter mark of subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

if percentage >= 60:
    print("First Class")
elif percentage >= 50:
    print("Second Class")
elif percentage >= 40:
    print("Pass Class")
else:
    print("Fail")
