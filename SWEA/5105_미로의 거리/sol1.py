import sys

sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    queue = []
    queue.append((sr, sc))
    visited[sr][sc] = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if maze[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[cr][cc] + 1   # 거리 측정을 위해 지나는 통로의 visited 값를 하나씩 늘려줌
                if maze[nr][nc] == 3:
                    return visited[cr][cc] - 1              # 시작점의 visited 값이 1이므로 1을 빼준 값이 거리가 됨
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c   # 시작점 찾기

    ans = BFS(sr, sc)
    print(f'#{tc} {ans}')
