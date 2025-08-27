import random


correct_user = "user1"
correct_pass = "pass123"


username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_user and password == correct_pass:
    code = random.randint(1000, 9999)
    print("Verification Code:", code)
    
    
    entered_code = input("Re-enter the code show ")
    
    if entered_code == str(code):
        print("Access Granted ")
    else:
        print("Verification Failed ")
else:
    print("Login Denied ")
