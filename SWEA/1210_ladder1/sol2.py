import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    for c in range(100):
        if ladder[r][c] == 2:
            break

    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    d = 0

    while r > 0:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < 100 and 0 <= nc < 100:
            if ladder[nr][nc] == 1:
                r = nr
                c = nc
                ladder[nr][nc] = 0
        d = (d+1) % 3

    print(f'#{tc} {c}')