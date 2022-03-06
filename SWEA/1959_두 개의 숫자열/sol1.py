import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0
    # N과 M 중 어느 쪽이 긴지 먼저 판단한다.
    if N < M:
        # 짧은 숫자열을 움직일 때 시작점은 0~M-N이 된다.
        for i in range(M-N+1):
            total = 0
            # 짧은 숫자열은 자신의 길이만큼만 돌고
            # 긴 숫자열은 짧은 숫자열의 시작점을 고려해야 한다.
            for j in range(N):
                total += A[j]*B[i+j]
            if max_v < total:
                max_v = total
    else:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += A[i+j]*B[j]
            if max_v < total:
                max_v = total

    print(f'#{tc} {max_v}')

