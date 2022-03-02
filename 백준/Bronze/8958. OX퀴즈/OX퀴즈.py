T = int(input())

for _ in range(T):
    result = input()
    score = cnt = 0
    for i in result:
        if i == 'O':
            cnt += 1
            score += cnt
        elif i == 'X':
            cnt = 0
            score += cnt
    print(score)

    

