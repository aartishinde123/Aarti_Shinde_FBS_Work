# Write a program to reverse three-digit number.

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

reverse_digit = d1*100 + d2*10 + d3
#display result
print(f'Reversing  {temp} digit is :{reverse_digit}')