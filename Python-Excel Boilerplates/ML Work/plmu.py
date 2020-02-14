test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    a = input().split(' ')
    a = [int(i) for i in a]
    count = 0
    # # Logic - 1, Bruteforce
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if a[i] * a[j] == a[i] + a[j]:
    #             count += 1

    # Logic - 2, Constants Approach
    num_count = a.count(0)
    if num_count > 1:
        count = int(0.5 * num_count * (num_count - 1))
    num_count = a.count(2)
    if num_count > 1:
        count += int(0.5 * num_count * (num_count - 1))
    print(count)
