import sys

sys.stdin = open('in1.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    for r in range(N):
        for c in range(N):
            each_sum = flies[r][c]

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                for m in range(1, M):
                    nr = r + dr[i] * m
                    nc = c + dc[i] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        each_sum += flies[nr][nc]
            if maxV < each_sum:
                maxV = each_sum

            dr = [1, 1, -1, -1]
            dc = [1, -1, -1, 1]
            each_sum = flies[r][c]
            for i in range(4):
                for m in range(1, M):
                    nr = r + dr[i] * m
                    nc = c + dc[i] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        each_sum += flies[nr][nc]
                if maxV < each_sum:
                    maxV = each_sum
    print(f'#{tc} {maxV}')

