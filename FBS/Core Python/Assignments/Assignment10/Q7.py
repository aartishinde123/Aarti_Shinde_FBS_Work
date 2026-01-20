# Write a program to create a new list from existing list which contains cube of each number of list.

list = [1, 2, 3, 4, 5]

cube_list = []


for i in list:
    cube_list.append(i * i * i)

print("Original list:", list)
print("Cube list:", cube_list)
