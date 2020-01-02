class Node:
    inorder_traversal = []
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
    def show_inorder(self):
        if self.left is not None:
            self.left.show_inorder()
        print(self.data, end=' ')
        Node.inorder_traversal.append(self.data)
        if self.right is not None:
            self.right.show_inorder()

class DLL:
    start = None
    end = None
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        if DLL.start is None:
            DLL.start = self
            DLL.end = self
        else:
            DLL.end = self
    def add(self, data):
        if self.right is not None:
            self.right.add(data)
        else:
            self.right = DLL(data)
    def show_dll_ltr(self):
        print(self.data, end=' ')
        if self.right is not None:
            self.right.show_dll_ltr()
    def show_dll_rtl(self):
        for data_node in self.fetch_dll_rtl():
            print(data_node, end=' ')
    def fetch_dll_rtl(self):
        if self.right is not None:
            data_nodes = self.right.fetch_dll_rtl()
            data_nodes.append(self.data)
            return data_nodes
        else:
            return [self.data]

def init_class_var():
    Node.inorder_traversal = []
    DLL.start = None
    DLL.end = None

def convert_bt_to_dll(bt):
    tree_nodes = Node.inorder_traversal
    tree_nodes = [int(node) for node in tree_nodes]
    dll = DLL(tree_nodes[0])
    for node in tree_nodes[1:]:
        dll.add(node)
    return dll

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
    print(f'Binary Tree:', end=' ')
    tree.show_inorder()
    print()
    dll = convert_bt_to_dll(tree)
    print(f'Double Linked List:')
    print(f'LTR: ',end=' ')
    dll.show_dll_ltr()
    print()
    print(f'RTL:', end=' ')
    dll.show_dll_rtl()
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    # OUTPUT                                    #
    # ['3', '4', '5', '6', '1', '2']            #
    # ['8', '4', '5', '6', '7', '2']            #
    #############################################
