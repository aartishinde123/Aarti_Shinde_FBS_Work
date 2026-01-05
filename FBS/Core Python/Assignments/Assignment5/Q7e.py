#e. x - x2/3 + x3/5 - x4/7 + .... to n terms

x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
den = 1

for i in range(1, n + 1):
    sum = sum + sign * (x ** i) / den
    sign = -sign
    den = den + 2

print("Sum =", sum)
