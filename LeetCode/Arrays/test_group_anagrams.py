import unittest
from unittest import TestCase
from group_anagrams import group_anagram

class Test(TestCase):
    def test_group_anagram(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = [["nat","tan"], ["bat"],["ate","eat","tea"]]

        self.assertEqual(group_anagram(strs).sort(key=lambda x: len(x)),
                         result.sort(key=lambda x: len(x)))

if __name__ == "__main__":
    unittest.main()