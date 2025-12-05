# WAP to print Armstrong number within a given range
# An Armstrong Number is a number whose sum of cubes of its digits is equal to the number.

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

for num in range(start, stop+1):
    temp = num

    # count digits
    count = 0
    while temp > 0:
        temp = temp // 10
        count += 1

    # calculate Armstrong sum
    temp = num
    sum = 0
    while temp > 0:
        d = temp % 10
        temp = temp // 10

        # power logic (same as your code)
        mult = 1
        for i in range(count):
            mult = mult * d

        sum = sum + mult

    # check Armstrong
    if sum == num:
        print(num)