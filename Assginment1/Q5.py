P = float(input("Enter Principal: "))
T = float(input("Enter Time: "))
R = float(input("Enter Rate: "))
CI = P * (1 + R/100)**T - P
print("Compound Interest =", CI)
