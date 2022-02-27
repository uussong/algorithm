import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    max_sum = 0

    # 내림차순 정렬
    for i in range(N-1, 0, -1):
        for j in range(i):
            if scores[j] < scores[j+1]: # < 방향 주의
                scores[j], scores[j+1] = scores[j+1], scores[j]

    # 최대 총점
    for i in range(K):
        max_sum += scores[i]

    print(f'#{tc} {max_sum}')

