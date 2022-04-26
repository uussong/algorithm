import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # 최대로 이동할 수 있는 정류장 수 K, 종점 N, 충전기 설치된 정류장 수 N
    charge = list(map(int, input().split()))
    station = [0] * (N+1)
    charge_cnt = 0 # 충전 횟수
    now = K # 일단 K로 최대로 이동

    # 충전기 설치된 정류장 표시
    for c in charge:
        station[c] = 1

    cnt = 0 # while문 돈 횟수 카운트
    while now < N:
        cnt += 1
        if cnt >= N:
            print(f'#{tc} 0')
            break

        if station[now] == 1:
            charge_cnt += 1
            now += K
        else:
            now -= 1
    if cnt < N:
        print(f'#{tc} {charge_cnt}')

