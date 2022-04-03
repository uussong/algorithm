import sys

sys.stdin = open('sample_input.txt')

def dfs(s, cnt, acc):
    global result
    # 백트래킹
    if acc > result:
        return

    if cnt == N:
        result = min(result, acc)
        return
    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                dfs(s+1, cnt+1, acc+arr[s][w])
                visited[w] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 999999
    dfs(0, 0, 0)
    print(f'#{tc} {result}')

