test_cases = int(input())
for test in range(test_cases):
    a = '0b' + input()
    b = '0b' + input()
    c = int(a, 2)
    d = int(b, 2)
    count = 0
    # Logic - 1 : Bruteforce - 50% Correct
    while d > 0:
        u = c ^ d
        v = c & d
        c = u
        d = v * 2
        # print(u, v, c, d)
        count += 1
    print('Count:', count)
    c = int(a, 2)
    d = int(b, 2)
    count = 0

    # Logic - 2 : Formulae Based - Wrong
    if d == 0:
        count = 0
    elif c < d:
        count = 1
    else:
        while c > d:
            c = c - d
            d = d * 2
            count += 1
            print(c, d, count)
        count += 2
    print('Count:', count)
