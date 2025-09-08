n = int(input("Enter number of students: "))
total_percent = 0

for i in range(n):
    marks = 0
    for j in range(5):
        m = int(input(f"Enter marks of subject {j+1}: "))
        marks += m
    percent = marks / 5
    print("Percentage of student", i+1, "=", percent)
    total_percent += percent

print("Average Percentage =", total_percent / n)
