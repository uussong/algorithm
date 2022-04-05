from collections import deque
import sys

sys.stdin = open('sample_input.txt')

def bfs(n, cnt):
    global result

    queue = deque()
    queue.append((n, cnt))
    visited.add(n)

    while queue:
        n, cnt = queue.popleft()
        if n == M:  # 종료 조건
            result = cnt
            return

        # 계산 하기
        if n+1 not in visited and n+1 <= 1000000:
            queue.append((n+1, cnt+1))
            visited.add(n+1)
        if n-1 not in visited and n-1 <= 1000000:
            queue.append((n-1, cnt+1))
            visited.add(n-1)
        if n*2 not in visited and n*2 <= 1000000:
            queue.append((n*2, cnt+1))
            visited.add(n*2)
        if n-10 not in visited and n-10 <= 1000000:
            queue.append((n-10, cnt+1))
            visited.add(n-10)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = set()
    result = 0
    bfs(N, 0)

    print(f'#{tc} {result}')
