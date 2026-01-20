# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

# Accept number of elements
n = int(input("Enter number of elements: "))

my_list = []

# Accept list elements
for i in range(n):
    num = int(input("Enter element: "))
    my_list.append(num)

even_list = []
odd_list = []

# Separate even and odd elements
for i in my_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Original list:", my_list)
print("Even elements list:", even_list)
print("Odd elements list:", odd_list)
