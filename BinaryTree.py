class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add(self, root, data, direction):
        if root == self.data:
            if direction == 'L' and self.left is None:
                self.left = Node(data)
                # print(f'\t\tAdded Node {nodes[i*3+1]} in Left of {nodes[i*3]}')
            elif direction == 'L':
                # print(f'\tNode {self.data} Already Has A Left Child.')
            elif direction == 'R' and self.right is None:
                self.right = Node(data)
                # print(f'\t\tAdded Node {nodes[i*3+1]} in Right of {nodes[i*3]}')
            elif direction == 'R':
                # print(f'\tNode {self.data} Already Has A Right Child.')
            else:
                # print(f'\t{direction} Is Unknown Direction')
                pass
            return True
        else:
            if self.left is not None:
                # print(f'\tGoing In Left Of {self.data}')
                flag_1 = self.left.add(root, data, direction)
                if flag_1:
                    return
            if self.right is not None:
                # print(f'\tGoing In Right Of {self.data}')
                flag_2 = self.right.add(root, data, direction)
                if flag_2:
                    return
            return
    def delete(self, data):
        # Logic Not Created
        pass
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

testcases = int(input())
for test in range(testcases):
    #########################################
    # Input Format as                       #
    # 1 2 L 1 3 R                           #
    # Where 1 2 L means "2 is in left of 1" #
    #########################################
    edge_count = int(input())
    nodes = input().split(' ')
    # print(f'Adding Root Node: {nodes[0]}')
    tree = Node(nodes[0])
    for i in range(edge_count):
        root, data, direction = nodes[i*3], nodes[i*3+1], nodes[i*3+2]
        # if nodes[i*3+2] == 'L':
        #     print(f'Adding {nodes[i*3+1]} in Left of {nodes[i*3]}')
        # if nodes[i*3+2] == 'R':
        #     print(f'Adding {nodes[i*3+1]} in Right of {nodes[i*3]}')
        tree.add(root, data, direction)
    tree.show_in()
    print()
    tree.show_pre()
    print()
    tree.show_post()
