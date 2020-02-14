from itertools import permutations
from itertools import product

test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    a = input()
    b = input()
    p_a = list(set([i for i in permutations(list(a))]))
    p_b = list(set([i for i in permutations(list(b))]))
    count = 0
    xor = []
    # # Logic - 1 : Bruteforce : 10%
    # for i in range(len(p_a)):
    #     m = '0b' + ''.join(j for j in p_a[i])
    #     for j in range(len(p_b)):
    #         n = '0b' + ''.join(k for k in p_b[j])
    #         x = int(m, 2) ^ int(n, 2)
    #         xor.append(x)

    # Logic - 2 : Simplified : 10%
    p_a = ['0b' + ''.join(j for j in i) for i in p_a]
    p_b = ['0b' + ''.join(j for j in i) for i in p_b]
    xor = [int(i[0], 2) ^ int(i[1], 2) for i in product(p_a, p_b)]
    print(len(list(set(xor))))
