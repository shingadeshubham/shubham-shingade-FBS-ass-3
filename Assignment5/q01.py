uid = "admin"
pwd = "1234"

for i in range(3):
    u = input("Enter User ID: ")
    p = input("Enter Password: ")
    if u == uid and p == pwd:
        print("Login Successful")
        break
    else:
        print("Wrong, try again")
else:
    print("3 attempts over")
