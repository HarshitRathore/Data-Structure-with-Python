class Node:
    root = None
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add(self, data):
        if self.left is None:
            print(f'Inserting {data} in left of {self.data}')
            self.left = Node(data)
            return True
        elif self.right is None:
            print(f'Inserting {data} in right of {self.data}')
            self.right = Node(data)
            return True
        else:
            isAdd = False
            while not isAdd:
                print(f'Sending {data} in left down of {self.data}')
                isAdd = self.left.add(data)
                if not isAdd:
                    print(f'Sending {data} in right down of {self.data}')
                    isAdd = self.right.add(data)
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
            1
          2   3
         4 5 6 7
"""

tree = Node(1)
Node.root = 1
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.show_in()
print()
tree.show_pre()
print()
tree.show_post()
