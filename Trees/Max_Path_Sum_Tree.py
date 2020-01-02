# Maximum Path Sum in a Binary Tree to be calculated between 2 leaf nodes

from itertools import combinations

class Node:
    root = None
    leaf_nodes = []
    root_path = {}
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data, parent=self)
                self.gen_path(self.left)
            else:
                self.right = Node(data, parent=self)
                self.gen_path(self.right)
            return True
        else:
            if self.left is not None:
                if self.left.add(root, data, direction):
                    return
            if self.right is not None:
                if self.right.add(root, data, direction):
                    return
            return
    def gen_path(self, node):
        path = []
        node_data = node.data
        while node.parent != None:
            path.insert(0, node.data)
            node = node.parent
        path.insert(0, node.data)
        Node.root_path[(Node.root, node_data)] = path
    def get_leaf_nodes(self):
        if self.left is None and self.right is None:
            Node.leaf_nodes.append(self.data)
        else:
            if self.left is not None:
                self.left.get_leaf_nodes()
            if self.right is not None:
                self.right.get_leaf_nodes()
    def lca_sum(self, node_1, node_2):
        path_1 = Node.root_path[(Node.root, node_1)][:]
        path_2 = Node.root_path[(Node.root, node_2)][:]
        i = 0
        common_ancestor = None
        while True:
            if path_1[i] == path_2[i]:
                common_ancestor = path_1[i]
            if path_1[i+1] == path_2[i+1]:
                path_1.pop(i)
                path_2.pop(i)
            else:
                break
            i += 1
            if i == len(path_1)-1 or i == len(path_2)-1:
                break
        sum = 0
        for i in path_1 + path_2[1:]:
            sum += i
        return sum
    def path_sum(self):
        sum = []
        self.get_leaf_nodes()
        print(Node.root_path)
        for node_1, node_2 in combinations(Node.leaf_nodes, 2):
            found_sum = self.lca_sum(node_1, node_2)
            sum.append(found_sum)
        return max(sum)

def init_class_var():
    Node.root = None
    Node.leaf_nodes = {}
    Node.level_dict = {}
    Node.root_path = {}

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
        if nodes[i] not in 'LR':
            nodes[i] = int(nodes[i])
    tree = Node(nodes[0])
    Node.root = nodes[0]
    for i in range(edge_count):
        root, data, direction = nodes[i*3], nodes[i*3+1], nodes[i*3+2]
        tree.add(root, data, direction)
    print(f'{tree.path_sum()}')
    init_class_var()
    ######################################################################################
    # INPUT TEST CASES                                                                   #
    # 2                                                                                  #
    # 6                                                                                  #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R                                                #
    # 12                                                                                  #
    # -15 5 L -15 6 R 5 -8 L 5 1 R -8 2 L -8 -3 R 6 3 L 6 9 R 9 0 R 0 4 L 0 -1 R -1 10 L #
    # OUTPUT                                                                             #
    # 13                                                                                 #
    # 27                                                                                 #
    ######################################################################################
