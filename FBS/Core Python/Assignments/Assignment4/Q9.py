# WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter a number:"))
for i in range(1,20):
    if(i % n == 0):
        print(i)