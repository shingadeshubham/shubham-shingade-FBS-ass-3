num = int(input("Enter number of employees: "))
total_salary_all = 0

for i in range(1, num + 1):
    basic = int(input(f"Enter basic salary of employee {i}: "))
    
    if basic < 20000:
        total_salary = basic + 0.10*basic + 0.12*basic + 0.15*basic
    else:
        total_salary = basic + 0.15*basic + 0.18*basic + 0.20*basic
    
    print(f"Total salary of employee {i}: {total_salary}")
    total_salary_all += total_salary

print(f"Total salary of all employees: {total_salary_all}")
