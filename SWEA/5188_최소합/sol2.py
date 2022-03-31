import sys

sys.stdin = open('sample_input.txt')

dr = [1, 0] # 하 우
dc = [0, 1]

def dfs(r, c, ssum):
    global min_sum
    if min_sum < ssum:
        return

    if r == N-1 and c == N-1:
        ssum += matrix[r][c]
        if min_sum > ssum:
            min_sum = ssum
            return
    else:
        for d in range(2):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                dfs(nr, nc, ssum+matrix[r][c])



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 999999
    ssum = 0
    dfs(0, 0, ssum)
    print(f'#{tc} {min_sum}')

