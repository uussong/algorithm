bowl = list(input())

rlt = 10
for i in range(len(bowl)-1):
    if bowl[i] == bowl[i+1]:
        rlt += 5
    else:
        rlt += 10

print(rlt)