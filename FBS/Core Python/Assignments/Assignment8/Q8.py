# Write a program find reverse of a number

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

num = int(input("Enter number: "))
print("Reverse of number:", reverse_number(num))
