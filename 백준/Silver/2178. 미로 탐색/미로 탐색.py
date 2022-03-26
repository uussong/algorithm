dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]

def BFS():
    queue = []
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if maze[nr][nc] == 1:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1
    return visited[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

ans = BFS()

print(ans)