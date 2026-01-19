# Write a program to reverse a number using recursion.

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
print("Reversed number is:", reverse_number(num))
