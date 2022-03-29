import sys

sys.stdin = open('input.txt')

def bfs(S):
    queue = []
    queue.append(S)
    visited[S] = 1
    sol = S
    while queue:
        c = queue.pop(0)
        # 마지막 방문지 중 숫자가 가장 큰 것이 답
        if visited[sol] < visited[c] or visited[sol] == visited[c] and sol < c:
            sol = c

        for i in range(1, 101):
            if graph[c][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[c] + 1
    return sol

T = 10
for tc in range(1, T + 1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    visited = [0] * 101
    # 인접행렬
    graph = [[0]* 101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        graph[lst[i]][lst[i+1]] = 1

    ans = bfs(S)

    print(f'#{tc} {ans}')

