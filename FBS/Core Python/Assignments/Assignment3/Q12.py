# Write a program to check if given 3 digit number is a palindrome or not.

# take input
num = int(input('Enter three digit number:'))
temp = num
# separate digits
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

# Reverse the number
rev = d1*100 + d2*10 + d3

if temp == rev:
    print("It is a palindrome number.")
else:
    print("It is NOT a palindrome number.")
