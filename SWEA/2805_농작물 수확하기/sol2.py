import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    center = N // 2

    total = sum1 = sum2 = 0
    for r in range(N):
        if r <= center:
            for c in range(center-r, center+r+1):
                sum1 += farm[r][c]
        else:
            for c in range(r-center, N-(r-center)):
                sum2 += farm[r][c]

    total = sum1 + sum2

    print(f'#{tc} {total}')

