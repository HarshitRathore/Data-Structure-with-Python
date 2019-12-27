class Node:
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
    def show_in(self):
        if self.left:
            self.left.show_in()
        print(self.data, end=', ')
        if self.right:
            self.right.show_in()
    def show_pre(self):
        print(self.data, end=', ')
        if self.left:
            self.left.show_pre()
        if self.right:
            self.right.show_pre()
    def show_post(self):
        if self.left:
            self.left.show_post()
        if self.right:
            self.right.show_post()
        print(self.data, end=', ')
    def check_bst(self):
        result = self.val_comparator(self.data)
        if result:
            print(f'Tree is a BST.')
        else:
            print(f'Tree is Not a BST.')
    def val_comparator(self, root, direction=None):
        if self.data == root and direction is None:
            # print(f'Going Down, Root Node')
            return self.go_down(self.data)
        elif self.data < root and direction == 'L':
            # print(f'Going Down, Node {self.data} in Left of {root}')
            return self.go_down(self.data)
        elif self.data < root:
            # print(f'Escaping, Node {self.data} in Left of {root}')
            return False
        elif self.data > root and direction == 'R':
            # print(f'Going Down, Node {self.data} in Right of {root}')
            return self.go_down(self.data)
        elif self.data > root:
            # print(f'Escaping, Node {self.data} in Right of {root}')
            return False
    def go_down(self, root):
        if self.left is not None:
            # print(f'Node {self.data} Left Child Found')
            result = self.left.val_comparator(self.data, 'L')
            if not result:
                return False
        if self.right is not None:
            # print(f'Node {self.data} Right Child Found')
            result = self.right.val_comparator(self.data, 'R')
            if not result:
                return False
        return True

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

    # tree.show_in()
    # print()
    # tree.show_pre()
    # print()
    # tree.show_post()
    # print()
    
    tree.check_bst()

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
