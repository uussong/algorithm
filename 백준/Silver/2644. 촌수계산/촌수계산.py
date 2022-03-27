def bfs():
    queue = []
    queue.append(p1)
    visited[p1] = 1

    while queue:
        c = queue.pop(0)
        for i in range(1, N+1):
            if graph[c][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[c] + 1
    if visited[p2]:
        return visited[p2]-1
    else:
        return -1

N = int(input())
p1, p2 = map(int, input().split())
M = int(input())
line = [list(map(int, input().split())) for _ in range(M)]
visited = [0] * (N+1)
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for each in line:
    start = each[0]
    end = each[1]

    graph[start][end] = 1
    graph[end][start] = 1

ans = bfs()
print(ans)