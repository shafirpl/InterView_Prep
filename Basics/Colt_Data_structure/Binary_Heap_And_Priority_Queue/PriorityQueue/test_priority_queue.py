import unittest
from priorityQueue import PriorityQueue


class PriorityQueueTest(unittest.TestCase):
    def test_enqueue(self):
        priority_queue = PriorityQueue()
        priority_queue.enqueue(10, 6)
        priority_queue.enqueue(20, 5)
        priority_queue.enqueue(30, 4)
        priority_queue.enqueue(40, 3)
        priority_queue.enqueue(50, 2)
        priority_queue.enqueue(60, 1)
        priority_queue.enqueue(70, 0)

        self.assertEqual([{0: 70}, {3: 40}, {1: 60}, {6: 10}, {4: 30}, {5: 20}, {2: 50}], priority_queue.returnQueue())

    def test_dequeue(self):
        priority_queue = PriorityQueue()
        priority_queue.enqueue(10, 6)
        priority_queue.enqueue(20, 5)
        priority_queue.enqueue(30, 4)
        priority_queue.enqueue(40, 3)
        priority_queue.enqueue(50, 2)
        priority_queue.enqueue(60, 1)
        priority_queue.enqueue(70, 0)

        returned_node = priority_queue.dequeue()
        self.assertEqual(70, returned_node.get_value())
        self.assertEqual([{1: 60}, {3: 40}, {2: 50}, {6: 10}, {4: 30}, {5: 20}], priority_queue.returnQueue())


if __name__ == "__main__":
    unittest.main()
