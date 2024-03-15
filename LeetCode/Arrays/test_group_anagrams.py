import unittest
from unittest import TestCase
from group_anagrams import group_anagram

class Test(TestCase):
    def test_group_anagram(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = [["bat"],["nat","tan"],["ate","eat","tea"]]

        self.assertEqual(group_anagram(strs), result)

if __name__ == "__main__":
    unittest.main()