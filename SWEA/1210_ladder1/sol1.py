import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 델타 값
    d_r = [-1, 0, 0] #상, 좌, 우
    d_c = [0, -1, 1]
    direction = 0

    # 도착점인 2에서부터 올라가 출발점를 찾아가는 방식이므로 row index를 99로 두고
    r = 99
    # 반복문을 통해 출발점의 column index값을 할당한다.
    for i in range(100):
        if ladder[r][i] == 2:
            c = i

    while True:
        # 출발점 즉 row index가 0이 되면 반복을 멈춘다.
        if r == 0:
            break
        # 위로 올라갈 때
        if direction == 0:
            # 왼쪽 값이 1이라면 (column index가 0일 때 왼쪽 값이 없으므로 범위 설정해줌)
            if c > 0 and ladder[r][c-1] == 1:
                # 왼쪽 방향으로 향한다.
                direction = 1
            # 오른쪽 값이 1이라면 (column index가 99이 때 오른쪽 값이 없으므로 범위 설정해줌) 
            elif c < 99 and ladder[r][c+1] == 1:
                # 오른쪽 방향으로 향한다.
                direction = 2
        # 왼쪽으로 갈 때
        elif direction == 1:
            # 위쪽 값이 1이라면
            if ladder[r-1][c] == 1:
                # 위쪽 방향으로 향한다.
                direction = 0
        # 그 외 오른쪽으로 갈 때
        else:
            # 위쪽 값이 1이라면
            if ladder[r-1][c] == 1:
                # 위쪽 방향으로 향한다.
                direction = 0

        # r, c값에 변화하는 델타값을 할당해준다.
        r = r + d_r[direction]
        c = c + d_c[direction]

    print(f'#{tc} {c}') # 출발점의 column index 출력

