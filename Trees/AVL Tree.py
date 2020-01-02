class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1
        self.balance = 0
    def __repr__(self):
        return f"(Left:{self.left}|Right:{self.right}|Data:{self.data}|Height:{self.height}|Balance:{self.balance})"
    def insert(self,data):
        print("Inserting",data)
        if data < self.data:
            if self.left is None:
                print('#1')
                self.left = Node(data)
            else:
                print('#2')
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                print('#3')
                self.right = Node(data)
            else:
                print('#4')
                self.right.insert(data)
        self.height = 1 + max(
            self.left.height if self.left is not None else 0,
            self.right.height if self.right is not None else 0,
        )
        self.balance = self.right.height if self.right is not None else 0 - self.left.height if self.left is not None else 0
        # Left Left Rotation
        if self.balance < -1 and data < self.left.data:
            # print("Left Left Rotation")
            # print(self.__repr__())
            return self.rightRotate(self)            
        # Left Right Rotation
        if self.balance < -1 and data > self.left.data:
            # print("Left Right Rotation")
            # print(self.__repr__())
            self.left = self.leftRotate(self.left)
            return self.rightRotate(self)            
        # Right Right Rotation
        if self.balance > 1 and data > self.right.data:
            # print("Right Right Rotation")
            # print(self.__repr__())
            return self.leftRotate(self)            
        # Right Left Rotation
        if self.balance > 1 and data < self.right.data:
            # print("Right Left Rotation")
            # print(self.__repr__())
            self.right = self.rightRotate(self)
            return self.leftRotate(self)            
    def leftRotate(self,node):
        print("left rotate",node)
        y = node.right
        T2 = y.left
        # Performing rotation
        y.left = node
        node.right = T2
        # Updating heights
        node.height = 1 + max(
            node.left.height if node.left is not None else 0,
            node.right.height if node.right is not None else 0,
        )
        y.height = 1 + max(
            y.left.height if y.left is not None else 0,
            y.right.height if y.right is not None else 0,
        )
        print(y)
        return y
    def rightRotate(self,node):
        print("right rotate",node)
        y = node.left
        T3 = y.right
        # Performing rotation
        y.right = node
        node.left = T3
        # Updating heights
        node.height = 1 + max(
            node.left.height if node.left is not None else 0,
            node.right.height if node.right is not None else 0,
        )
        y.height = 1 + max(
            y.left.height if y.left is not None else 0,
            y.right.height if y.right is not None else 0,
        )
        print(y)
        return y
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
bt = Node(10)

# Inserting items
for i in [20,30,40,50,25]:
    bt.insert(i)

# Traversing the tree
print("Inorder :")
bt.show()
print()
print("Preorder :")
bt.preorder()
print()
print("Postorder :")
bt.postorder()
print()