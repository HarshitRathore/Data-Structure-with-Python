testcases = int(input())
for test in range(testcases):
    # Input Format as
    # 1 2 L 1 3 R
    # Where 1 2 L means "2 is in left of 1"
    edge_count = int(input())
    nodes = input().split(' ')
    print(f'Root Node: {nodes[0]}')
    for i in range(edge_count):
        if nodes[i*3+2] == 'L':
            print(f'{nodes[i*3+1]} in Left of {nodes[i*3]}')
        if nodes[i*3+2] == 'R':
            print(f'{nodes[i*3+1]} in Right of {nodes[i*3]}')
