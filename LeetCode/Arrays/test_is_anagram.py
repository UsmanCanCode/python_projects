import unittest

import LeetCode.Arrays.is_anagram as ia


class TestIsAnagram(unittest.TestCase):

    def test_is_anagram(self):
        a: str = "anagram"
        b: str = "margana"
        self.assertEqual(ia.is_anagram(a,b), True)

    def test_is_anagram_2(self):
        a: str = "anagram"
        b: str = "margan"
        self.assertEqual(ia.is_anagram2(a,b), False)

    def test_is_anagram_2_1(self):
        a: str = "horse"
        b: str = "roseh"
        self.assertEqual(ia.is_anagram2(a,b), True)

    def test_is_anagram_3(self):
        a: str = "anagram"
        b: str = "margan"
        self.assertEqual(ia.is_anagram3(a,b), False)

    def test_is_anagram_3_1(self):
        a: str = "horse"
        b: str = "roseh"
        self.assertEqual(ia.is_anagram3(a,b), True)

if __name__ == '__main__':
    unittest.main()
