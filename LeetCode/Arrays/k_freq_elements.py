# Given an integer array nums and an integer k, return the k most
# frequent elements. You may return the answer in any order.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
from collections import Counter


def top_k_element(arrays: [int], k: int) -> [int]:
    count: dict = {}
    result: [int] = []
    for int in nums:
        if int in count.keys():
            count[int] += 1
        else:
            count[int] = 1

    sorted_dict_list = sorted(count.items(), key=lambda x: x[1], reverse=True)

    if len(sorted_dict_list) >= k:

        for i in range(k):
            result.append(sorted_dict_list[i][0])

    return result

nums = [1,5,5,5,3,3,3,3,3,3,10,10,10,10,1,10,1,0,0,10,1,0,1,0,1010,10,10,
        10,10,10]
k = 6

print(top_k_element(nums, k))