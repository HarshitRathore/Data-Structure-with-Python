class Node:
    level_hd_data_list = {}
    def __init__(self, data, hd=0, level=0):
        self.left = None
        self.right = None
        self.data = data
        self.hd = hd
        self.level = level
        try:
            Node.level_hd_data_list[level].append((self.data, self.hd, self.level))
        except:
            Node.level_hd_data_list[level] = [(self.data, self.hd, self.level)]
    def __repr__(self):
        return f'(Data: {self.data} | Level: {self.level} | HD: {self.hd})'
    def add(self, root, data, direction):
        if root == self.data:
            if direction == 'L' and self.left is None:
                self.left = Node(data, self.hd-1, self.level+1)
            elif direction == 'R' and self.right is None:
                self.right = Node(data, self.hd+1, self.level+1)
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
    def show_detailed(self):
        if self.left:
            self.left.show_detailed()
        print(self, end=', ')
        if self.right:
            self.right.show_detailed()
    def show_bottom_view(self):
        all_levels = list(Node.level_hd_data_list.keys())
        all_hd = []
        bottom_nodes = []
        for i in list(Node.level_hd_data_list.values()):
            for j in i:
                all_hd.append(j[1])
        all_levels.sort(reverse=True)
        all_hd = list(set(all_hd))
        for i in all_levels:
            remove_hd = []
            for j in Node.level_hd_data_list[i]:
                if j[2] == max(all_levels):
                    bottom_nodes.append(j[0])
                    remove_hd.append(j[1])
                else:
                    if j[1] in all_hd:
                        bottom_nodes.append(j[0])
                        remove_hd.append(j[1])
            for j in list(set(remove_hd)):
                all_hd.remove(j)
        print(bottom_nodes)


def init_class_var():
    Node.level_hd_data_list = []

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
    tree.show_bottom_view()
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
