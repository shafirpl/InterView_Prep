from unittest import TestCase
from Stack import ArrayBasedStack, LinkedListBasedStack


class TestArrayBasedStack(TestCase):

    def test_pop(self):
        testStack = ArrayBasedStack()
        testStack.push(10)
        testStack.push(20)
        testStack.push(30)

        self.assertEqual(testStack.pop(), 30)

    def test_search(self):
        test_stack = ArrayBasedStack()

        test_stack.push(10)
        test_stack.push(20)
        test_stack.push(30)

        self.assertTrue(test_stack.search(20))
        self.assertFalse(test_stack.search(50))


class TestLinkedListBasedStack(TestCase):

    def test_pop(self):
        test_stack = LinkedListBasedStack()
        test_stack.push(10)
        test_stack.push(20)
        test_stack.push(30)
        self.assertEqual(test_stack.pop(), 30)

    def test_search(self):
        test_stack = LinkedListBasedStack()
        test_stack.push(10)
        test_stack.push(20)
        test_stack.push(30)

        self.assertTrue(test_stack.search(30))
        self.assertFalse(test_stack.search(50))
