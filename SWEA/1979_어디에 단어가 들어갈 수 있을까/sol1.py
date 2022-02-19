import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())) + [0]) # 범위체크를 따로 하지 않기위해 0으로 puzzle을 두름
    puzzle.append([0]*(N+1))
    rlt = 0
    # 행방향 체크
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    rlt += 1
                cnt = 0
    
    # 열방향 체크
    for j in range(N+1):
        cnt = 0
        for i in range(N+1):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    rlt += 1
                cnt = 0
    print(f'#{tc} {rlt}')

