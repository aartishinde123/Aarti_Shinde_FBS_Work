# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

# Function to count digits
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# Function to calculate Armstrong sum
def armstrong_sum(n, digits):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10
    return total

# Function to check Armstrong number
def is_armstrong(num):
    digits = count_digits(num)
    total = armstrong_sum(num, digits)
    return total == num

# Main program
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")
