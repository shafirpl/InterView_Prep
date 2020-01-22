import unittest
from BinarySearch import binary_search, binary_search_index, binary_search_iter

class BinaryTest(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([], 3),False)
        self.assertEqual(binary_search([1, 2], 3), False)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), True)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), True)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), True)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), True)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), True)

    def test_binary_search_index(self):
        self.assertEqual(binary_search_index([], 3), -1)
        self.assertEqual(binary_search_index([1, 2], 3), -1)
        self.assertEqual(binary_search_index([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_index([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_index([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_index([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_index([1, 2, 3, 4], 4), 3)

    def test_binary_search_iter(self):
        self.assertEqual(binary_search_iter([], 3), -1)
        self.assertEqual(binary_search_iter([1, 2], 3), -1)
        self.assertEqual(binary_search_iter([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_iter([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search_iter([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search_iter([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search_iter([1, 2, 3, 4], 4), 3)

if __name__ == "__main__":
    unittest.main()