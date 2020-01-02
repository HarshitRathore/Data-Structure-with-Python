class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data    
    def insert(self,data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
    # def remove(self, data):
    #     if data < self.data:
    #         self.left.remove(data)
    #     elif data > self.data:
    #         self.right.remove(data)
    #     else:
    #         # if self.left is None and self.right is None:
    #         #     self.data = ''
    #         if self.left is None:
    #             self.data = self.right
    #             return
    #         elif self.right is None:
    #             self.data = self.left
    #             return
    #         current = self.right
    #         while current.left is not None:
    #             current = current.left
    #         self.data = current.data
    #         self.right.remove(self.right.data)
    #         return
    def find(self,data):
        if data == self.data:
            print(f"Found {data} in this binary tree.")
        elif data < self.data and self.left is not None:
            self.left.find(data)
        elif data > self.data and self.right is not None:
            self.right.find(data)
        else:
            print(f"{data} not found in this binary tree.")
    def show(self):
        if self.left:
            self.left.show()
        print(self.data, end=' ')
        if self.right:
            self.right.show()
    def preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.show()
        if self.right:
            self.right.show()
    def postorder(self):
        if self.left:
            self.left.show()
        if self.right:
            self.right.show()
        print(self.data, end=' ')

# Created the node
bt = Node(3)

# Inserting items
for i in [7,2,5,4,0,9]:
    bt.insert(i)

# Traversing the tree
print("Inorder :")
bt.show()
print("Preorder :")
bt.preorder()
print()
print("Postorder :")
bt.postorder()
print()

# Finding the elements in the tree
bt.find(3)
bt.find(9)
bt.find(10)
bt.find(-1)
