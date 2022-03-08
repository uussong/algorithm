n = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for r in range(x, x+10):
        for c in range(y, y+10):
            paper[r][c] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)