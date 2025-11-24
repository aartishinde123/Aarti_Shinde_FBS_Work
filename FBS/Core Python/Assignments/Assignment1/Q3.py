#Program to find quotient and remainder of two numbers.

# Taking input from user
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))

# Calculating quotient and remainder
quotient = num1 // num2
remainder = num1 % num2

# Displaying the result
print("Quotient =", quotient)
print("Remainder =", remainder)