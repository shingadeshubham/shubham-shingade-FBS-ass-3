def sum_power_series(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i
    return total


n = int(input("Enter n: "))
print("Sum of power series =", sum_power_series(n))
