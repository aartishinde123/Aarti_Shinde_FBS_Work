# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

nums = [2, 4, 3, 5, 7, 8, 9]
target = 10

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print("Pairs with sum", target, "are:", pairs)
