class Node:
    hd_dict = {}
    def __init__(self, data, hd=0):
        self.data = data
        self.left = None
        self.right = None
        self.hd = hd
        try:
            Node.hd_dict[hd].append(data)
        except:
            Node.hd_dict[hd] = [data]
    def __repr__(self):
        return f'Data: {self.data} | HD: {self.hd}'
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data, hd=self.hd-1)
            else:
                self.right = Node(data, hd=self.hd+1)
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
    def show_inorder(self):
        if self.left is not None:
            self.left.show_inorder()
        print(self.data, end=', ')
        if self.right is not None:
            self.right.show_inorder()
    def show_vertically(self):
        all_hd = list(Node.hd_dict.keys())
        all_hd.sort()
        for hd in all_hd:
            for node in Node.hd_dict[hd]:
                print(node, end=' ')

def init_class_var():
    Node.hd_dict = {}

testcases = int(input())
for test in range(testcases):
    #########################################
    # Input Format as                       #
    # 1 2 L 1 3 R                           #
    # Where 1 2 L means "2 is in left of 1" #
    #########################################
    edge_count = int(input())
    nodes = input().split(' ')
    tree = Node(nodes[0])
    for i in range(edge_count):
        root, data, direction = nodes[i*3], nodes[i*3+1], nodes[i*3+2]
        tree.add(root, data, direction)
    tree.show_vertically()
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    # OUTPUT                                    #
    # 3 1 0 4 5 2 6                             #
    # 4 2 1 5 6 3 8 7                           #
    #############################################
