N = int(input())
matrix = [[0] * 1001 for _ in range(1001)]

for n in range(1, N+1):
    x, y, width, height = map(int, input().split())

    for r in range(x, x+width):
        for c in range(y, y+height):
            matrix[r][c] = n

cnt = [0] * (N+1)
for r in range(1001):
    for c in range(1001):
        if matrix[r][c]:
            cnt[matrix[r][c]] += 1

for i in range(1, N+1):
    print(cnt[i])