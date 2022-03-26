import sys

sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    queue = []
    queue.append((sr, sc))
    visited[sr][sc] = 1

    while queue:
        cr, cc = queue.pop(0)
        for d in range(4):
            nr, nc = cr + dr[d], cc + dc[d]
            if 0 <= nr < 100 and 0 <= nc < 100 and visited[nr][nc] == 0:
                if maze[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                if maze[nr][nc] == 3:
                    return 1
    return 0



T = 10
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]

    ans = BFS(1, 1)
    print(f'#{tc} {ans}')

