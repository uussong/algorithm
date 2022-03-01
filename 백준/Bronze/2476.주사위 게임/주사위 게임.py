N = int(input())
rlt = [] 
for _ in range(N):
    dice = list(map(int, input().split()))
    dice.sort()


    if dice[0] == dice[1] == dice[2]:
        rlt.append(10000 + dice[0] * 1000)
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        rlt.append(1000 + dice[1] * 100)
    elif dice[0] != dice[1] != dice[2]:
        rlt.append(dice[2] * 100)

print(max(rlt))
