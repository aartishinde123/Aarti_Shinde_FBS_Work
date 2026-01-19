# 1^1 + 2^2 + 3^3+ ...... n^n

def sum_power(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i ** i)
    return total

n = int(input("Enter n: "))
print("Sum of power series =", sum_power(n))
