# Write a program to swap two numbers without using third variable.

# take input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, " b =", b)

a,b=b,a
print("After swapping: a =", a, " b =", b)