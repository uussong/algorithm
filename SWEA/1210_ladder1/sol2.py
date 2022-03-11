import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    for i in range(100):
        if ladder[99][i] == 2:
            c = i

    d_row = [-1, 0, 0]
    d_col = [0, -1, 1]
    d = 0

    while r > 0:
        if d == 0:
            if c > 0 and ladder[r][c - 1] == 1:
                d = 1
            elif c < 99 and ladder[r][c + 1] == 1:
                d = 2
        else:
            if ladder[r - 1][c] == 1:
                d = 0

        r += d_row[d]
        c += d_col[d]
    print(f'#{tc} {c}')

