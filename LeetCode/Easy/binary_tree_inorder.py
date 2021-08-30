class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

class Solution:
    def inorderTraversal(self, root: Node) -> list[int]:
        self.ls = []
        self.printInOrder(root)
        return self.ls
    def printInOrder(self, node: Node):
        if node is None:
            return
        else:
            # going onto the left child
            self.printInOrder(node.left)
            self.ls.append(node.val)
            # going onto the right child
            self.printInOrder(node.right)