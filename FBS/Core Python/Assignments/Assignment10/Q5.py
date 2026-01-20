# Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.


li = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter the number to search: "))

count = 0


for i in li:
    if i == num:
        count = count + 1

if count > 0:
    print(num, "is present in the list")
    print("It is present", count, "times")
else:
    print(num, "is NOT present in the list")
