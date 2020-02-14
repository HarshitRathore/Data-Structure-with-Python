test_cases = int(input())
for test in range(test_cases):
    n = input()
    flag = False
    mapping = {
        '1': '1',
        '2': '7',
        '3': '8',
        '4': '5',
        '6': '9',
        '7': '2',
        '8': '3',
        '5': '4',
        '9': '6'
    }
    if len(n) == 1:
        flag = True
    if '0' in n:
        flag = False
    elif len(n) != 1:
        odd = True if len(n) % 2 != 0 else False
        part_1 = ''
        part_2 = ''
        if odd:
            part_1 = n[0:len(n)//2]
            part_2 = n[len(n)//2+1:]
            part_2 = part_2[::-1]
        else:
            part_1 = n[0:len(n)//2]
            part_2 = n[len(n)//2:]
            part_2 = part_2[::-1]
        # print(part_1, part_2)
        for i in range(len(n)//2):
            # print(f'Comparing {part_1[i]} and {mapping[part_2[i]]}')
            if part_1[i] == mapping[part_2[i]]:
                flag = True
            else:
                flag = False
                break
    if flag:
        print('true')
    else:
        print('false')
