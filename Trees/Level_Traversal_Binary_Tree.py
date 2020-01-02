class Node:
    # Variable for Level Wise Nodes
    level_nodes = {}
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add(self, root, data, direction):
        if root == self.data:
            if direction == 'L' and self.left is None:
                self.left = Node(data)
            elif direction == 'R' and self.right is None:
                self.right = Node(data)
            return True
        else:
            if self.left is not None:
                flag_1 = self.left.add(root, data, direction)
                if flag_1:
                    return
            if self.right is not None:
                flag_2 = self.right.add(root, data, direction)
                if flag_2:
                    return
            return
    def show_level(self):
        self.traverse_levels()
        for level, nodes in Node.level_nodes.items():
            for node in nodes:
                print(node, end=' ')
            print()
    def traverse_levels(self, level=0):
        # print(f'Level: {level} | Node: {self.data} | Level_Nodes: {Node.level_nodes}')
        try:
            Node.level_nodes[level].append(self.data)
        except Exception as e:
            Node.level_nodes[level] = []
            Node.level_nodes[level].append(self.data)
        if self.left is not None:
            self.left.traverse_levels(level+1)
        if self.right is not None:
            self.right.traverse_levels(level+1)

def init_class_var():
    Node.level_nodes = {}

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
    tree.show_level()
    init_class_var()
    #######################################
    # INPUT TEST CASES                    #
    # 2                                   #
    # 6                                   #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R #
    # 6                                   #
    # 3 1 L 1 0 L 1 2 R 3 5 R 5 4 L 5 6 R #
    # OUTPUT                              #
    # Tree is a BST.                      #
    # Tree is Not a BST.                  #
    #######################################
