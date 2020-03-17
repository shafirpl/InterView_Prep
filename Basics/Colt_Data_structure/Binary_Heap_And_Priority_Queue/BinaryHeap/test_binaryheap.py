import unittest
from binaryheap import BinaryMaxHeap


class TestBinaryMaxHeap(unittest.TestCase):
    def test_insert(self):
        binary_heap = BinaryMaxHeap()
        binary_heap.insert(10)
        binary_heap.insert(20)
        binary_heap.insert(30)
        binary_heap.insert(40)
        binary_heap.insert(50)
        binary_heap.insert(60)
        binary_heap.insert(70)

        self.assertEqual([70, 40, 60, 10, 30, 20, 50], binary_heap.return_heap())

    def test_remove(self):
        binary_heap = BinaryMaxHeap()
        binary_heap.insert(10)
        binary_heap.insert(20)
        binary_heap.insert(30)
        binary_heap.insert(40)
        binary_heap.insert(50)
        binary_heap.insert(60)
        binary_heap.insert(70)

        binary_heap.extract_max()
        self.assertEqual([60, 40, 50, 10, 30, 20], binary_heap.return_heap())

        binary_heap.extract_max()
        self.assertEqual([50, 40, 20, 10, 30], binary_heap.return_heap())

        binary_heap.extract_max()
        self.assertEqual([40, 30, 20, 10], binary_heap.return_heap())

        binary_heap.extract_max()
        self.assertEqual([30, 10, 20], binary_heap.return_heap())

        binary_heap.extract_max()
        self.assertEqual([20, 10], binary_heap.return_heap())

        binary_heap.extract_max()
        self.assertEqual([10], binary_heap.return_heap())


if __name__ == "__main__":
    unittest.main()
