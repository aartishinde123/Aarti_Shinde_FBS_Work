#Write a program to print first n prime numbers.

n = int(input("Enter value of n: "))

num = 2
while n > 0:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        n -= 1   # reduce n when a prime is found
    num += 1
