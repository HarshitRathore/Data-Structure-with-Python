class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
        else:
            self.data = data
    def show_leaf(self):
        if self.left is None and self.right is None:
            print(self.data, end=', ')
        if self.left:
            self.left.show_leaf()
        if self.right:
            self.right.show_leaf()

"""
Creating Following BST
            3
         /     \
        1       5
         \     / \
          2   4   8
                 /
                7
"""

tree = Node(3)
tree.add(1)
tree.add(2)
tree.add(5)
tree.add(4)
tree.add(8)
tree.add(7)
tree.show_leaf()
