import unittest
from QuickSort import quickSort

class BubbleSortTest(unittest.TestCase):

    def test_quickSort(self):
        self.assertEqual(quickSort([8,1,2,3,4,5,6,7]),[1,2,3,4,5,6,7,8])
        self.assertEqual(quickSort([10,5,90,0,10]), [0,5,10,10,90])
        self.assertEqual(quickSort([64, 34, 25, 22, 11, 90,12]), [11,12,22,25,34,64,90])
        self.assertEqual(quickSort([8,90,4,1,5,5]), [1,4,5,5,8,90])
        self.assertEqual(quickSort([1, 2, 3, 4, 5, 5]), [1, 2, 3, 4, 5, 5])


if __name__ == "__main__":
    unittest.main()
