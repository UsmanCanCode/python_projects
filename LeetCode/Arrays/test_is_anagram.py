import unittest

import LeetCode.Arrays.is_anagram as ia


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        a: str = "anagram"
        b: str = "margana"
        self.assertEqual(ia.is_anagram(a,b), True)

    def test_is_anagram2(self):
        a: str = "anagram"
        b: str = "margan"
        self.assertEqual(ia.is_anagram2(a,b), False)

if __name__ == '__main__':
    unittest.main()
