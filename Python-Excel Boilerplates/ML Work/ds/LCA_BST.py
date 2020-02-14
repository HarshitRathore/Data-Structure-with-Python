class Node:
    root = None
    paths = {}
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
        if (Node.root, data) in Node.paths.keys():
            Node.paths[(Node.root, data)].insert(-1, self.data)
        else:
            Node.paths[(Node.root, data)] = [Node.root, data]
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
        elif self.data < data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
        else:
            return
    def show_inorder(self):
        if self.left is not None:
            self.left.show_inorder()
        print(self.data, end=', ')
        if self.right is not None:
            self.right.show_inorder()
    def lca(self, node_1, node_2):
        path_1 = Node.paths[(Node.root, node_1)]
        path_2 = Node.paths[(Node.root, node_2)]
        found = False
        i = 0
        ancestor = None
        while not found:
            if path_1[i] == path_2[i]:
                ancestor = path_1[i]
                i += 1
            else:
                found = True
        print(f'Ancestor: {ancestor}')

def init_class_var():
    Node.root = None
    Node.paths = {}

testcases = int(input())
for test in range(testcases):
    #########################################
    # Input Format as                       #
    # 5 2 1 4 3 7                           #
    #########################################
    nodes = input().split(' ')
    node_1, node_2 = input().split(' ')
    node_1, node_2 = int(node_1), int(node_2)
    nodes =[int(node) for node in nodes]
    tree = Node(nodes[0])
    Node.root = nodes[0]
    for node in nodes[1:]:
        tree.add(node)
    tree.lca(node_1, node_2)
    init_class_var()
    ####################
    # INPUT TEST CASES #
    # 2                #
    # 3 1 5 0 2 4 6    #
    # 4 6              #
    # 3 1 5 0 2 4 6    #
    # 4 2              #
    # OUTPUT           #
    # 5                #
    # 3                #
    ####################
