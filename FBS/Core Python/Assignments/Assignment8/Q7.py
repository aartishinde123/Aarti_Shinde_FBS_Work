# Write a program to find sum of digits of a number.

def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n //= 10
    return sum

num = int(input("Enter number: "))
print("Sum of digits:", sum_of_digits(num))
