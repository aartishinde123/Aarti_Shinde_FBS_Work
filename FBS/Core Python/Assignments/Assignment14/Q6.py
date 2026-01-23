# Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. 
# Use the Python set.

nums = [1, 10, -5, 1, -100]

# remove duplicates using set
unique_nums = set(nums)

# convert back to list for indexing
unique_nums = list(unique_nums)

# initialize
max_product = unique_nums[0] * unique_nums[1]
pair = (unique_nums[0], unique_nums[1])

# check all pairs
for i in range(len(unique_nums)):
    for j in range(i + 1, len(unique_nums)):
        product = unique_nums[i] * unique_nums[j]
        if product > max_product:
            max_product = product
            pair = (unique_nums[i], unique_nums[j])

print("Pair with maximum product:", pair)
print("Maximum product:", max_product)
