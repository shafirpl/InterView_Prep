import unittest
from BinarySearch import binary_search_recursive,binary_search_iterative

class BinaryTest(unittest.TestCase):

    def test_binary_search_iterative(self):
        self.assertEqual(binary_search_iterative([], 3), -1)
        self.assertEqual(binary_search_iterative([1, 2], 3), -1)
        self.assertEqual(binary_search_iterative([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_iterative([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_iterative([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_iterative([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_iterative([1, 2, 3, 4], 4), 3)

    def test_binary_search_recursive(self):
        self.assertEqual(binary_search_recursive([], 3), -1)
        self.assertEqual(binary_search_recursive([1, 2], 3), -1)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_recursive([1, 2, 3, 4], 4), 3)

if __name__ == "__main__":
    unittest.main()