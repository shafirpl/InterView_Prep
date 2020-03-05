class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        queue = []
        visited = []

        queue.append(self.root)

        while (len(queue) != 0):
            visitedNode = queue.pop(0)
            visited.append(visitedNode.value)
            if visitedNode.left is not None:
                queue.append(visitedNode.left)
            
            if visitedNode.right is not None:
                queue.append(visitedNode.right)

        return visited


    def search(self, value):
        if self.root is None:
            return False

        current_root = self.root
        while(True):

            if current_root is None:
                return False

            elif value == current_root.value:
                return True

            else:
                if value > current_root.value:
                    current_root = current_root.right
                    continue

                else:
                    current_root = current_root.left
                    continue

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return

        current_root = self.root
        while(True):
            if value == current_root.value:
                return None
            if value > current_root.value:
                if current_root.right is None:
                    current_root.right = new_node
                    return
                else:
                    current_root = current_root.right
                    continue

            else:
                if current_root.left is None:
                    current_root.left = new_node
                    return
                else:
                    current_root = current_root.left
                    continue

    def remove(self, data):
        # if the tree is empty, return false
        if self.root is None:
            return False

        # if we are removing root node
        if data == self.root.value:
            # if there is only one node
            if self.root.right is None and self.root.left is None:
                self.root = None
                return True

            # if the root node only has one subchild
            if self.root.right is None and self.root.left is not None:
                old_root = self.root
                self.root = self.root.left
                old_root.left = None
                return True

            if self.root.left is None and self.root.right is not None:
                old_root = self.root
                self.root = self.root.right
                old_root.right = None
                return True

            # if the root node has both child
            # similar to what we do for other nodes with 2 child, find the minimum of right subtree and
            # replace with it

            if self.root.left is not None and self.root.right is not None:
                minNode = self.root.right
                parent_minNode = minNode

                while minNode.left is not None:
                    parent_minNode = minNode
                    minNode = minNode.left

                # transfer the value from minimum node of right subtree to deleted node
                self.root.value = minNode.value

                # delete  the min Node
                if self.root.right.left is not None:
                    parent_minNode.left = None

                return True

        # if we are removing some other node

        # first need to find the node that we want to delete
        current_node = self.root
        prev_node = self.root
        while current_node is not None and current_node.value != data:
            prev_node = current_node
            if(data > current_node.value):
                current_node = current_node.right
            else:
                current_node = current_node.left

        # if data not found
        if current_node is None:
            return False

        # now if data is found, 3 cases

        # first case, the deleted node is a leaf node
        if current_node.left is None and current_node.right is None:
            if data > prev_node.value:
                prev_node.right = None
                return True

            else:
                prev_node.left = None
                return True

        # second case, the deleted node has one child
        if current_node.left is None and current_node.right is not None:
            if data > prev_node.value:
                prev_node.right = current_node.right
                return True
            else:
                prev_node.left = current_node.right
                return True

        if current_node.right is None and current_node.left is not None:
            if data > prev_node.value:
                prev_node.right = current_node.left
                return True
            else:
                prev_node.left = current_node.left
                return True

        # if the deleted node has both left and right child
        if current_node.left is not None and current_node.right is not None:
            # find the minimum in right subtree
            # one trick, the minimum in the right subtree will be the lowest level node in left
            # draw a bst and see for myself
            # also all the min nodes will go to left side, so when looping we need to traverse through the left

            minNode = current_node.right
            parent_minNode = minNode

            while minNode.left is not None:
                parent_minNode = minNode
                minNode = minNode.left

            # transfer the value from minimum node of right subtree to deleted node
            current_node.value = minNode.value

            # delete  the min Node
            if current_node.right.left is not None:
                parent_minNode.left = None

            return True
