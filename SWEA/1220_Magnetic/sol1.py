import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]

    # 각 열별로 N극이 위 S극이 아래인 형태여야 교착 상태가 됨
    cnt = 0     # 교착 상태 개수
    for i in range(N):
        check = 0   # N극(1)을 만났을 때를 표시할 변수
        for j in range(N):
            if magnetic[j][i] == 1 and check == 0:
                check = 1
            elif magnetic[j][i] == 2 and check == 1:
                cnt += 1
                check = 0

    print(f'#{tc} {cnt}')

