import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    rlt = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            cnt = 0
            for i in range(r, r+M):
                for j in range(c, c+M):
                    cnt += lst[i][j]
            if rlt < cnt:
                rlt = cnt

    print(f'#{tc} {rlt}')

