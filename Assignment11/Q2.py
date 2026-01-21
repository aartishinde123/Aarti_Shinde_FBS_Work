# Python Program to Merge Two Lists and Sort it

# First list
list1 = [5, 2, 9, 1]

# Second list
list2 = [8, 3, 6, 4]

merged_list = []

# Merge list1
for i in list1:
    merged_list.append(i)

# Merge list2
for i in list2:
    merged_list.append(i)

# Sort the merged list (Bubble Sort)
n = len(merged_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if merged_list[j] > merged_list[j + 1]:
            temp = merged_list[j]
            merged_list[j] = merged_list[j + 1]
            merged_list[j + 1] = temp

print("Merged and sorted list:", merged_list)
