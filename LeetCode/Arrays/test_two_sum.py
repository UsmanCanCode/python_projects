import unittest

from LeetCode.Arrays.two_sum import istwosum


class Test(unittest.TestCase):
    def test_istwosum(self):
        array = [2, 7, 11, 15]
        target = 9
        self.assertEqual(istwosum(array, target), [0, 1])
    def test2_istwosum(self):
        array = [2, 0, 11, 15]
        target = 9
        self.assertEqual(istwosum(array, target), [])

if __name__ == "__main__":
    unittest.main()
