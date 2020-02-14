test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    s = input()
    s_ = s * n
    count = 0
    x = ''
    # # Logic - 1 : 30% Correct
    # for i in range(len(s)-1):
    #     if s[i] == s[i+1] and s[i] == 'S':
    #         count += 1
    # count *= n
    # if s[0] == 'S' and s[-1] == 'S':
    #     count += (n-1)
    
    # Logic - 2 : Wrong
    flag = False
    for i in s:
        if i in 'S':
            flag = True
            x += i
        else:
            if flag:
                x += '_'
                flag = False
    print(x)
    for i in range(len(x)-1):
        if x[i] == x[i+1] and x[i] == 'S':
            count += 1
    count *= n
    if x[0] == 'S' and x[-1] == 'S':
        count += (n-1)
    print(count)
