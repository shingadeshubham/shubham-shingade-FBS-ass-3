marks = []
for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5
print("Percentage =", percentage)