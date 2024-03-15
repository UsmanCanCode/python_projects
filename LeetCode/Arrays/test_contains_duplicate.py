import unittest


from LeetCode.Arrays.contains_duplicate import contains_duplicate


class Test(unittest.TestCase):
    def test_contains_duplicate(self):
        array: [int] = [1, 2, 3, 4, 5]
        self.assertEqual(contains_duplicate(array), False)

    def test_contains_duplicate2(self):
        array: [int] = [1, 2, 1, 3, 4]
        self.assertEqual(contains_duplicate(array), True)

    def test_contains_duplicate3(self):
        array: [int] = []
        self.assertEqual(contains_duplicate(array), False)

if __name__ == '__main__':
    unittest.main()