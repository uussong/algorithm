import sys

sys.stdin = open('input.txt')

def dfs(s, per):
    global max_per
    
    # 백트래킹
    if per <= max_per:
        return

    if s == N:  # 종료조건
        max_per = max(per, max_per)
        return
    
    else:
        for w in range(N):
            if not visited[w]:
                visited[w] = 1
                dfs(s+1, per*(arr[s][w]/100))
                visited[w] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    max_per = 0
    dfs(0, 1)
    
    print(f'#{tc} {max_per*100:.6f}')

