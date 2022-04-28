N = int(input())
target = int(input())

arr = [[0] * N for _ in range(N)]

r = c = 0
dr = [1, 0, -1, 0] # 하 우 상 좌
dc = [0, 1, 0, -1]
d = 0
cnt = 0
while cnt < N**2:
    arr[r][c] = N**2 - cnt
    cnt += 1
    nr, nc = r + dr[d], c + dc[d]
    
    if nr < 0 or nc < 0 or nr >= N or nc >= N or arr[nr][nc]:
        d = (d+1) % 4  
    r += dr[d]
    c += dc[d]
for i in arr:
    print(*i)

for r in range(N):
    for c in range(N):
        if arr[r][c] == target:
            print(r+1, c+1)
