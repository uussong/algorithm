import sys

sys.stdin = open('sample_input.txt')

def dfs(x, y, acc):
    global result

    if x == N-1 and y == N-1:   # 종료 조건
        result = min(acc, result)
    else:
        if x + 1 < N:   # 아래로 움직이는 경우
            dfs(x + 1, y, acc + arr[x + 1][y])
        if y + 1 < N:   # 오른쪽으로 움직이는 경우
            dfs(x, y + 1, acc + arr[x][y + 1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 999999

    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')

