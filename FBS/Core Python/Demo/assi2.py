#WAP to calculate sum of digit of 3 digit number

# take input
num = int(input('Enter three digit number:'))
temp = num
# separate digit
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3
print(f'Addition of{temp} digits is{sum}:')