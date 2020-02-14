class Node:
    level_dict = {}
    def __init__(self, data, level=0):
        self.data = data
        self.left = None
        self.right = None
        self.level = level
        try:
            Node.level_dict[level].append(data)
        except:
            Node.level_dict[level] = [data]
    def add(self, root, data, direction):
        if self.data == root:
            if direction == 'L':
                self.left = Node(data, level=self.level+1)
            else:
                self.right = Node(data, level=self.level+1)
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
    def show_spirally(self):
        for k, v in Node.level_dict.items():
            if k % 2 == 0:
                for node in v[::-1]:
                    print(node, end=' ')
            else:
                for node in v:
                    print(node, end=' ')

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
    tree = Node(nodes[0])
    for i in range(edge_count):
        root, data, direction = nodes[i*3], nodes[i*3+1], nodes[i*3+2]
        tree.add(root, data, direction)
    tree.show_spirally()
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    # OUTPUT                                    #
    # 0 1 2 6 5 4 3                             #
    # 1 2 3 7 6 5 4 8                           #
    #############################################
