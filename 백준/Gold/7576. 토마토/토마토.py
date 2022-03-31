from collections import deque

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]
def bfs(sr, sc):
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            cr, cc = queue.popleft()
            for d in range(4):
                nr, nc = cr + dr[d], cc + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if tomato[nr][nc] == 0:
                        tomato[nr][nc] = 1
                        queue.append([nr, nc])

    for r in range(N):
        for c in range(M):
            if tomato[r][c] == 0:
                return -1
    else:
        return cnt - 1

M, N = map(int,input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
for r in range(N):
    for c in range(M):
        if tomato[r][c] == 1:
            queue.append([r, c])

print(bfs(r, c))