# Write a program to print list after removing even numbers.

list = [10, 15, 20, 25, 30, 35, 40]

new_list = []

# Keep only odd numbers
for i in list:
    if i % 2 != 0:
        new_list.append(i)

print("Original list:", list)
print("List after removing even numbers:", new_list)
