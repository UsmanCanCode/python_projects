# Given an array of strings strs, group the anagrams together. You can
# return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.


# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict


def group_anagram(array: [str]) -> [str]:
    groups: [str] = []

    group_key_val = {}

    for item in array:
        sorted_item = "".join(sorted(item))
        if sorted_item in group_key_val.keys():
            group_key_val[sorted_item].append(item)
        else:
            group_key_val[sorted_item] = [item]

    groups = group_key_val.values()

    return list(groups)


def group_anagram1(array: [str]) -> [str]:
    grouped: dict = defaultdict(list)

    for word in array:
        word_key = "".join(sorted(word))
        grouped[word_key].append(word)

    return list(grouped.values())
