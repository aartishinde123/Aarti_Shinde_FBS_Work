# Write a program to print all numbers which are divisible by m and n in the list.

list = [10, 12, 15, 20, 24, 30, 40]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Numbers divisible by", m, "and", n, "are:")

for i in list:
    if i % m == 0 and i % n == 0:
        print(i)
