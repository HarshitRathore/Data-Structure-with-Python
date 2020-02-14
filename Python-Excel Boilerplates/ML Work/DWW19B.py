test_cases = int(input())
for test in range(test_cases):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    a = input().split(' ')
    a = [int(i) for i in a]
    ans = {}
    def hcf(x, y):
        if x == 0:
            return y
        return hcf(y % x, x)
    a.sort()
    for i in a:
        new = (i * k) / hcf(i, k)
        ans[i] = new if new < 10 ** 18 else -1
    def sort_dict(x):
        min_ = min(x.values())
        comb = []
        for i in x.keys():
            if x[i] == min_:
                comb.append(int(x[i]))
        return comb
    print(ans)
    print(min(sort_dict(ans)))
