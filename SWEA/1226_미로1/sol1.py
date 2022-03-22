import sys

sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0] # 상 하 좌 우
dc = [0, 0, -1, 1]

def BFS(sr, sc):
    queue = []
    queue.append((sr, sc))  # 큐에 시작점 삽입
    visited[sr][sc] = 1     # 방문 배열에 시작점 방문 표시

    while queue:
        cr, cc = queue.pop(0)   # 큐에 첫 번째 원소 꺼냄
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0:  # 범위 및 방문 체크
                if maze[nr][nc] == 0:
                    queue.append((nr, nc))  # 통로라면 삽입과 방문 체크
                    visited[nr][nc] = 1
                if maze[nr][nc] == 3:       # 도착지라면 
                    return 1                # 도달 가능
    return 0    # 조건 만족 못 하면 도달 불가능 표시

T = 10
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0 for _ in range(16)] for _ in range(16)]

    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                sr, sc = r, c   # 시작점 구하기

    ans = BFS(sr, sc)

    print(f'#{tc} {ans}')

