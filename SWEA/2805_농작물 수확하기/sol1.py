import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    revenue = 0

    m = N // 2 # 중앙값

    # 마름모꼴 모양이기 때문에 너비가 늘어나는 부분과 줄어드는 부분을 나누어 계산
    # 늘어나는 부분 (r <= m)
    sum1 = 0
    for r in range(m+1):
        for c in range(m-r, m+r+1):
            sum1 += farm[r][c]

    # 줄어드는 부분 (r > m)
    sum2 = 0
    for r in range(m+1, N):
        for c in range(m-(N-r)+1, m+N-r):
            sum2 += farm[r][c]

    revenue = sum1 + sum2

    print(f'#{tc} {revenue}')

