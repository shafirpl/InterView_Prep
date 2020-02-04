import unittest
from Selection_Sort import selection_sort


class SelectionSortTest(unittest.TestCase):

    def test_Bubble_Sort(self):
        self.assertEqual(selection_sort([8, 1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(selection_sort([10, 5, 90, 0, 10]), [0, 5, 10, 10, 90])
        self.assertEqual(selection_sort([64, 34, 25, 22, 11, 90, 12]), [
                         11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(selection_sort([8, 90, 4, 1, 5, 5]), [1, 4, 5, 5, 8, 90])
        self.assertEqual(selection_sort(
            [0,1,5,2]), [0,1,2,5])


if __name__ == "__main__":
    unittest.main()
