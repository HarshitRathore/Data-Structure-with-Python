test_cases = int(input())
for test in range(test_cases):
    n, k = input().split(' ')
    n, k = int(n), int(k)
    a = input().split(' ')
    a = [int(i) for i in a]
    batch = []
    history = []
    for i in a:
        if len(batch) < k:
            batch.append(i)
            history.append(a.index(i))
        else:
            min_ = min(batch)
            if batch.count(min_) > 1:
                min_list = [k for k in batch if k == min(batch)]
                earliest = {}
                print(history)
                print(min_list)
                for j in min_list:
                    earliest[j] = history[::-1].index(j)
                print(earliest.values())
                min_ = min(earliest.values())
                for k,v in earliest.items():
                    if v == min_:
                        batch = [i^k if z==k else z for z in batch]
                        # batch.replace(k, i)
                        break
            else:
                batch = [i^min_ if z==min_ else z for z in batch]
                #batch.replace(min_, i)
    for i in batch:
        print(i, end=' ')
