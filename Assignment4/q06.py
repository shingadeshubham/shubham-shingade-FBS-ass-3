n = int(input("Enter number: "))
flag = True
if n < 2:
    flag = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = False
            break
if flag:
    print("Prime number")
else:
    print("Not a prime number")
