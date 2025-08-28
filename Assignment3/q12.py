num = int(input("Enter 3-digit number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
