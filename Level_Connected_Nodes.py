class Node:
    level_dict = {}
    def __init__(self, data, level=0):
        self.data = data
        self.left = None
        self.right = None
        self.level = level
        self.connected = None
        try:
            Node.level_dict[level].append(data)
        except:
            Node.level_dict[level] = [data]
    def __repr__(self):
        return f'Data: {self.data} | Left: {True if self.left is not None else False} | Right: {True if self.right is not None else False} | Connected: {self.connected.data if self.connected is not None else None}'
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data, level=self.level+1)
            else:
                self.right = Node(data, level=self.level+1)
            return True
        else:
            if self.left is not None:
                if self.left.add(root, data, direction):
                    return
            if self.right is not None:
                if self.right.add(root, data, direction):
                    return
            return
    def show_connected(self):
        if self.left is not None:
            self.left.show_connected()
        print(self)
        if self.right is not None:
            self.right.show_connected()
    def connect_nodes(self):
        for level, nodes in Node.level_dict.items():
            for node_index in range(len(nodes)-1):
                self.find_node(nodes[node_index]).connected = self.find_node(nodes[node_index + 1])
            self.find_node(nodes[len(nodes) - 1]).connected = None
    def find_node(self, data):
        if self.data == data:
            return self
        else:
            if self.left is not None:
                flag_1 = self.left.find_node(data)
                if flag_1 is not None:
                    return flag_1
            if self.right is not None:
                flag_2 = self.right.find_node(data)
                if flag_2 is not None:
                    return flag_2
            return

def init_class_var():
    Node.level_dict = {}

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
    tree.connect_nodes()
    tree.show_connected()
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    #############################################
