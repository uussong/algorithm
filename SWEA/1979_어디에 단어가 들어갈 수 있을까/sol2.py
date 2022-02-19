import sys

sys.stdin = open('input.txt')

# 1이 K개 있는 자리의 개수를 세는 함수
# 행/열 체크 중복 피하기 위해 함수를 만듦
def check_count(N):
    rlt = 0
    for i in range(N + 1):
        cnt = 0
        for j in range(N + 1):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    rlt += 1
                cnt = 0
    return rlt

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())) + [0])  # 범위체크를 따로 하지 않기위해 0으로 puzzle을 두름
    puzzle.append([0] * (N + 1))
    # 행방향 체크
    rlt = check_count(N)
    # puzzle의 행과 열을 바꿈
    puzzle = list(map(list, zip(*puzzle)))
    # 원래 puzzle의 열방향 체크해 누적
    rlt += check_count(N)

    print(f'#{tc} {rlt}')

