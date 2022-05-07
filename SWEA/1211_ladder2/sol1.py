import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    dr = [-1, 0, 0]  # 상, 좌, 우
    dc = [0, -1, 1]
    direction = 0

    min_cnt = 999999
    min_col = 100
    for i in range(100):
        # 시작점의 좌표를 구하는 것이므로 도착지부터 올라가는 형태
        if ladder[99][i] == 1:
            r, c = 99, i
            cnt = 1

            while r > 0:
                # 위로 올라갈 때 왼쪽 / 오른쪽이 1 이라면 방향 바꿔줌
                if direction == 0:
                    if c > 0 and ladder[r][c-1] == 1:
                        direction = 1
                    elif c < 99 and ladder[r][c+1] == 1:
                        direction = 2
                # 왼쪽/오른쪽으로 올라갈 때 위쪽이 1이라면 방향 바꿔줌
                elif direction == 1 or direction == 2:
                    if ladder[r-1][c] == 1:
                        direction = 0
                
                # r,c 좌표를 방향에 따라 갱신하고 cnt 하나씩 늘려줌
                r += dr[direction]
                c += dc[direction]
                cnt += 1

            # 도착했을 때 최소 거리를 구하고 그 때의 좌표를 구함
            if cnt < min_cnt:
                min_cnt = cnt
                min_col = c

    print(f'#{tc} {min_col}')