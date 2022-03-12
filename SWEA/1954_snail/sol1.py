import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    dr = [0, 1, 0, -1] # 우 하 좌 상
    dc = [1, 0, -1, 0]
    d = 0
    r = c = 0

    for num in range(1, N**2 + 1):
        matrix[r][c] = num
        nr = r + dr[d]
        nc = c + dc[d]
        
        # matrix에서 벗어나거나 값이 0이 아니라면
        if nr < 0 or nc < 0 or nr >= N or nc >= N or matrix[nr][nc] != 0:
            d = (d + 1) % 4 # 방향 바꿈

        r = r + dr[d]
        c = c + dc[d]

    print(f'#{tc} ')
    for i in matrix:
        print(*i)