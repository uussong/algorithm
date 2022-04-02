import sys

sys.stdin = open('sample_input.txt')

def dfs(s, cnt, acc):
    global result

    if acc >= result:   # 백트래킹
        return

    if cnt == N-1:  # 종료 조건
        acc += arr[s][0] # 마지막에 다시 1로 돌아가는 거니까 더해줌
        result = min(acc, result)
        return

    for w in range(1, N):
        if not visited[w]:
            visited[w] = 1 
            dfs(w, cnt+1, acc+arr[s][w])
            visited[w] = 0  # visited 초기화

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 999999
    dfs(0, 0, 0)
    print(f'#{tc} {result}')

