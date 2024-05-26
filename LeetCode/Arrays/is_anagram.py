# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise. An Anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the original
# letters exactly once.

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

def is_anagram(a: str, b: str) -> bool:
    if sorted(a) == sorted(b):
        return True
    return False


def is_anagram2(a: str, b: str) -> bool:
    A: dict = {}
    B: dict = {}

    for l in a:
        if l in A.keys():
            A[l] += 1
        else:
            A[l] = A.get(l, 0) + 1

    for l in b:
        if l in B.keys():
            B[l] += 1
        else:
            B[l] = B.get(l, 0) + 1

    return A == B


def is_anagram3(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False

    A: dict = {}
    B: dict = {}
    for l in a:
        A[l] = A.get(l, 0) + 1
    for l in b:
        B[l] = B.get(l, 0) + 1

    return A == B
