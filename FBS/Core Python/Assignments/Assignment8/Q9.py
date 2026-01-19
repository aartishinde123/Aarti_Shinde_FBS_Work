# Write a program to check if entered number is a palindrome or not.

def is_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return temp == rev

num = int(input("Enter number: "))
if is_palindrome(num):
    print("Palindrome number")
else:
    print("Not a Palindrome number")
