# Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

nums = [1, 2, -1, 0, -2, 1]
target = 0

nums.sort()          # sort to avoid duplicate combinations
result = set()       # store unique triplets

n = len(nums)

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        if current_sum == target:
            result.add((nums[i], nums[left], nums[right]))
            left += 1
            right -= 1

        elif current_sum < target:
            left += 1
        else:
            right -= 1

# print result
print("Unique combinations:")
for triplet in result:
    print(triplet)
