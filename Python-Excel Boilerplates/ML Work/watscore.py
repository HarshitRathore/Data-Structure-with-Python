test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    scores = {}
    total_score = 0
    for i in range(n):
        prob, score = input().split(' ')
        prob, score = int(prob), int(score)
        if prob == 9 or prob == 10 or prob == 11:
            pass
        else:
            if prob in scores.keys():
                if score > scores[prob]:
                    scores[prob] = score
            else:
                scores[prob] = score
    for i in list(scores.keys()):
        total_score += scores[i]
    print(total_score)
