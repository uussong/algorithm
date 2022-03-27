def BFS():
    queue = []
    queue.append(1)
    visited[1] = 1

    while queue:
        c = queue.pop(0)
        for i in range(1, N+1):
            if graph[c][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return visited.count(1)-1


N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터 쌍의 수
line = [list(map(int, input().split())) for _ in range(M)]
visited = [0] * (N+1)
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for each in line:
    start = each[0]
    end = each[1]

    graph[start][end] = 1
    graph[end][start] = 1

ans = BFS()
print(ans)