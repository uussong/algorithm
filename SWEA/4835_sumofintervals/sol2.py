import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_list = [] # 구간합 담을 리스트
    for i in range(N-M+1): # 구간합 시작 인덱스
        sum_list.append(sum(A[i:i+M])) # 시작 인덱스부터 이웃한 M개의 합 계산
                                       # 인덱스 슬라이싱 사용

    ans = max(sum_list) - min(sum_list)
    print(f'#{tc} {ans}')

