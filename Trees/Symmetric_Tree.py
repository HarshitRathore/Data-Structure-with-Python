# Inputs are different, take the logic only.

class Node:
    inorder = []
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data)
            else:
                self.right = Node(data)
            return True
        else:
            if self.left is not None:
                if self.left.add(root, data, direction):
                    return
                if self.right.add(root, data, direction):
                    return
            return
    def gen_inorder(self):
        if self.left is not None:
            self.left.gen_inorder()
        Node.inorder.append(self.data)
        if self.right is not None:
            self.right.gen_inorder()

def init_class_var():
    Node.inorder = []

testcases = int(input())
for test in range(testcases):
    #########################################
    # Input Format as                       #
    # 1 2 L 1 3 R                           #
    # Where 1 2 L means "2 is in left of 1" #
    #########################################
    edge_count = int(input())
    nodes = input().split(' ')
    for i in range(len(nodes)):
        if nodes[i] in '0123456789':
            nodes[i] = int(nodes[i])
    tree = Node(nodes[0])
    for i in range(edge_count):
        root, data, direction = nodes[i*3], nodes[i*3+1], nodes[i*3+2]
        tree.add(root, data, direction)
    # Main Logic
    tree.left.gen_inorder()
    left_inorder = Node.inorder
    init_class_var()
    tree.right.gen_inorder()
    right_inorder = Node.inorder
    if left_inorder == right_inorder:
        print(True)
    else:
        print(False)
    init_class_var()
