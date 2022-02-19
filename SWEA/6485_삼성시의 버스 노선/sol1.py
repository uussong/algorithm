import sys

sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0]*5001 # 1~5000까지의 버스정류장 번호
    for i in range(N):
        A, B = map(int, input().split())
        # A, B사이의 모든 정류장을 다니는 버스
        for j in range(A, B+1):
            cnt[j] += 1

    bus_stop = [] # 정류장마다 다니는 버스 개수 모으는 list
    P = int(input()) # 버스가 지나가는 정류장 개수
    # 버스가 지나가는 정류장 번호
    for i in range(P):
        C = int(input())
        bus_stop.append(cnt[C])

    rlt = ' '.join(map(str, bus_stop)) # str형으로 바꿔 처리
    print(f'#{tc} {rlt}')

