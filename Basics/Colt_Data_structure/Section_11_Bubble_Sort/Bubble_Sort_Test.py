import unittest
from Bubble_Sort import bubble_sort

class BubbleSortTest(unittest.TestCase):

    def test_Bubble_Sort(self):
        self.assertEquals(bubble_sort([8,1,2,3,4,5,6,7]),[1,2,3,4,5,6,7,8])
        self.assertEqual(bubble_sort([10,5,90,0,10]), [0,5,10,10,90])
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11,12,22,25,34,64,90])


if __name__ == "__main__":
    unittest.main()