# Write a program to accept 3 digit number. If first digit is double of second digit and half of third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

num = int(input("Enter three digit number:"))
temp = num

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num //10

if((2 * d1) == d2 == (0.5 * d3)):
    print("Yes, you have done it")
else:
    print("Please try next time")    
