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
    def delete(self, data):
        # Logic Not Created            
    def show_in(self):
        if self.left:
            self.left.show_in()
        print(self.data, end=', ')
        if self.right:
            self.right.show_in()
    def show_pre(self):
        print(self.data, end=', ')
        if self.left:
            self.left.show_pre()
        if self.right:
            self.right.show_pre()
    def show_post(self):
        if self.left:
            self.left.show_post()
        if self.right:
            self.right.show_post()
        print(self.data, end=', ')

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
tree.show_in()
print()
tree.show_pre()
print()
tree.show_post()
