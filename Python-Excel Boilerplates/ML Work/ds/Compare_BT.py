class Node:
    inorder = []
    preorder = []
    postorder = []
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
            if self.right is not None:
                if self.right.add(root, data, direction):
                    return
            return
    def gen_inorder(self):
        if self.left is not None:
            self.left.gen_inorder()
        Node.inorder.append(self.data)
        if self.right is not None:
            self.right.gen_inorder()
    def gen_preorder(self):
        Node.preorder.append(self.data)
        if self.left is not None:
            self.left.gen_preorder()
        if self.right is not None:
            self.right.gen_preorder()
    def  gen_postorder(self):
        if self.left is not None:
            self.left.gen_postorder()
        if self.right is not None:
            self.right.gen_postorder()
        Node.postorder.append(self.data)

def init_class_var():
    Node.inorder = []
    Node.preorder = []
    Node.postorder = []

testcases = int(input())
for test in range(testcases):
    #########################################
    # Input Format as                       #
    # 1 2 L 1 3 R                           #
    # Where 1 2 L means "2 is in left of 1" #
    #########################################
    edge_count_1 = int(input())
    nodes_1 = input().split(' ')
    for i in range(len(nodes_1)):
        if nodes_1[i] in '0123456789':
            nodes_1[i] = int(nodes_1[i])
    tree_1 = Node(nodes_1[0])
    for i in range(edge_count_1):
        root, data, direction = nodes_1[i*3], nodes_1[i*3+1], nodes_1[i*3+2]
        tree_1.add(root, data, direction)
    tree_1.gen_inorder()
    tree_1.gen_preorder()
    tree_1.gen_postorder()
    tree_1_inorder = Node.inorder
    tree_1_preorder = Node.preorder
    tree_1_postorder = Node.postorder
    init_class_var()
    edge_count_2 = int(input())
    nodes_2 = input().split(' ')
    for i in range(len(nodes_2)):
        if nodes_2[i] in '0123456789':
            nodes_2[i] = int(nodes_2[i])
    tree_2 = Node(nodes_2[0])
    for i in range(edge_count_2):
        root, data, direction = nodes_2[i*3], nodes_2[i*3+1], nodes_2[i*3+2]
        tree_2.add(root, data, direction)
    tree_2.gen_inorder()
    tree_2.gen_preorder()
    tree_2.gen_postorder()
    tree_2_inorder = Node.inorder
    tree_2_preorder = Node.preorder
    tree_2_postorder = Node.postorder
    print(tree_1_inorder, tree_1_preorder, tree_1_postorder, tree_2_inorder, tree_2_preorder, tree_2_postorder, sep='\n')
    if tree_1_inorder == tree_2_inorder and tree_1_preorder == tree_2_preorder and tree_1_postorder == tree_2_postorder:
        print('1')
    else:
        print('0')
    init_class_var()
    #############################################
    # INPUT TEST CASES                          #
    # 2                                         #
    # 6                                         #
    # 0 1 L 1 3 L 1 4 R 0 2 R 2 5 L 2 6 R       #
    # 7                                         #
    # 1 2 L 1 3 R 2 4 L 2 5 R 3 6 L 3 7 R 6 8 R #
    #############################################
