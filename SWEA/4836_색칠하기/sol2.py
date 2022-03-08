import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if color == 1:
                    grid[r][c] += 1
                elif color == 2:
                    grid[r][c] += 2

    cnt = 0
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
