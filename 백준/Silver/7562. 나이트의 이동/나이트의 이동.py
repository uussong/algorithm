dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]
def bfs(start_r, start_c, end_r, end_c):
    queue = []
    queue.append([start_r, start_c])
    chess[start_r][start_c] = 1
    while queue:
        r, c = queue.pop(0)

        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < L and 0 <= nc < L and chess[nr][nc] == 0:
                queue.append([nr, nc])
                chess[nr][nc] = chess[r][c] + 1

        if r == end_r and c == end_c:
            return chess[end_r][end_c]-1

T = int(input())
for _ in range(T):
    L = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())
    chess = [[0]*L for _ in range(L)]

    ans = bfs(start_r, start_c, end_r, end_c)
    print(ans)