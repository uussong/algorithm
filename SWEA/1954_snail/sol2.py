from pprint import pprint
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    dr = [0, 1, 0, -1]  # 우 하 좌 상
    dc = [1, 0, -1, 0]

    r = c = d = 0
    num = 1

    while num <= N**2:
        snail[r][c] = num
        nr, nc = r + dr[d], c + dc[d]
        num += 1

        if nr < 0 or nc < 0 or nr >= N or nc >= N or snail[nr][nc]:
            d = (d+1) % 4

        r += dr[d]
        c += dc[d]


    print(f'#{tc} ')
    for each in snail:
        print(*each)

