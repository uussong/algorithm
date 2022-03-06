dice = list(map(int, input().split()))
dice.sort()

rlt = 0 
if dice[0] == dice[1] == dice[2]:
    rlt = 10000 + dice[0] * 1000
elif dice[0] == dice[1] or dice[1] == dice[2]:
    rlt = 1000 + dice[1] * 100
elif dice[0] != dice[1] != dice[2]:
    rlt = dice[2] * 100

print(rlt)
