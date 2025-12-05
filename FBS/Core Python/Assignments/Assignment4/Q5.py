# WAP to print Fibonacci series upto n.

n = int(input("Enter how many terms you want: "))

a = -1
b = 1

print("Fibonacci Series:")

for i in range(n):
    #print(a)
    c = a + b
    print(c)
    a = b
    b = c
