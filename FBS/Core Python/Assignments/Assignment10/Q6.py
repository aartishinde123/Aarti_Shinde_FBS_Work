# Write a program to remove duplicates from the list.

li = [10, 20, 10, 30, 20, 40]

new_list = []

for i in li:
    found = 0
    for j in new_list:
        if i == j:
            found = 1
            break
    if found == 0:
        new_list.append(i)

print("List after removing duplicates:", new_list)
