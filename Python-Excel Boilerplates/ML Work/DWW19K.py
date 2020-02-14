import math

test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    a = input().split(' ')
    a = [int(i) for i in a]
    summation = 0
    for i in a:
        summation += i
    p = (1 / (10 * n * math.pi)) * summation
    print(p)
