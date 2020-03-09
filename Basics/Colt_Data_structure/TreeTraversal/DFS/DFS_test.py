import unittest
from DFS import BinarySearchTree


class BinarySearchTreeTest(unittest.TestCase):

    def testSearch(self):
        tree = BinarySearchTree()
        self.assertFalse(tree.search(10))
        tree.insert(10)
        tree.insert(20)
        tree.insert(5)
        tree.insert(15)
        tree.insert(30)
        tree.insert(6)
        tree.insert(4)
        tree.insert(29)
        tree.insert(8)

        self.assertTrue(tree.search(10))
        self.assertTrue(tree.search(20))
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(15))
        self.assertTrue(tree.search(30))
        self.assertTrue(tree.search(6))
        self.assertTrue(tree.search(4))

        self.assertFalse(tree.search(100))

        self.assertFalse(tree.remove(100))

        # removing a leaf node
        self.assertTrue(tree.remove(4))
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(6))

        # removing a node with 2 children
        self.assertTrue(tree.remove(20))
        self.assertFalse(tree.search(20))
        self.assertTrue(tree.search(29))
        self.assertTrue(tree.search(15))
        self.assertTrue(tree.search(30))

        # removing a node with 1 child
        self.assertTrue(tree.remove(6))
        self.assertTrue(tree.search(8))

    def test_root_remove(self):
        tree = BinarySearchTree()
        tree.insert(10)
        self.assertTrue(tree.remove(10))
        self.assertFalse(tree.search(10))

        tree.insert(10)
        tree.insert(20)
        self.assertTrue(tree.remove(10))
        self.assertFalse(tree.search(10))
        self.assertTrue(tree.search(20))

        self.assertTrue(tree.remove(20))

        tree.insert(10)
        tree.insert(20)
        tree.insert(5)
        tree.insert(25)
        tree.insert(11)

        self.assertTrue(tree.remove(10))
        self.assertEqual(tree.root.value, 11)
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(20))
        self.assertTrue(tree.search(25))
        self.assertFalse(tree.search(10))

    def test_PreOrder(self):
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(6)
        tree.insert(15)
        tree.insert(3)
        tree.insert(8)
        tree.insert(20)


        self.assertEqual(tree.preOrder(),[10,6,3,8,15,20])
        # print(tree.preOrder())

    def testPostOrder(self):
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(6)
        tree.insert(15)
        tree.insert(3)
        tree.insert(8)
        tree.insert(20)

        self.assertEqual(tree.postOrder(), [3,8,6,20,15,10])

    def testinOrder(self):
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(6)
        tree.insert(15)
        tree.insert(3)
        tree.insert(8)
        tree.insert(20)

        self.assertEqual(tree.inOrder(), [3, 6, 8, 10, 15, 20])

        


if __name__ == "__main__":
    unittest.main()
