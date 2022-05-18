import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    max_score = 0

    scores.sort(reverse=True)

    for i in range(K):
        max_score += scores[i]

    print(f'#{tc} {max_score}')

