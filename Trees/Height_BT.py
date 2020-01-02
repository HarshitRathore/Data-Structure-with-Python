class Node:
    height = 0
    def __init__(self, data, height=1):
        self.data = data
        self.left = None
        self.right = None
        self.height = height
        Node.height = height
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data, height=self.height+1)
            else:
                self.right = Node(data, height=self.height+1)
            return True
        else:
            if self.left is not None:
                if self.left.add(root, data, direction):
                    return
            if self.right is not None:
                if self.right.add(root, data, direction):
                    return
            return

def init_class_var():
    Node.height = 0

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
    print(f'Height of tree is {Node.height}')
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    # OUTPUT                                    #
    # 3                                         #
    # 4                                         #
    #############################################
