test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    a = input().split(' ')
    a = [int(i) for i in a]
    def find_hcf(x, y):
        if x == 0:
            return y
        return find_hcf(y % x, x)
    hcf = find_hcf(a[0], a[1])
    # print(f'hcf: {hcf} of {a[0]} and {a[1]}')
    for i in range(2, n):
        hcf = find_hcf(hcf, a[i])
        # print(f'hcf: {hcf} of {hcf} and {a[i]}')
        if hcf == 1:
            break
    total_price = 0
    for i in a:
        total_price += i // hcf
    print(hcf, total_price)
