# Given an array of integers nums and an integer target, return indices of
# the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.
#
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

def two_sum(nums: [int], target) -> [int]:
    """
    trying brute force
    return index of the solution
    """
    for i in range(0, len(nums)):
        for k in range(i+1, len(nums)):
            if (nums[i] + nums[k]) == target:
                return [i, k]

    return []



def istwosum(array: [int], target: int) -> [int]:

    seen: dict = {}

    for i in range(len(array)):
        complement = target - array[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[array[i]] = i

    return []

