#!/usr/bin/python3

nums = [2,3, 4, 2, 7, 8]
duplicate = 0

for i in range(len(nums)):
    for j in range((i+1), len(nums)):
        if nums[i] == nums[j]:
            duplicate = nums[i]
            break

print(duplicate)
