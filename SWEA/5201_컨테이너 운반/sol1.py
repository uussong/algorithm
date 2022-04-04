import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    weights.sort(reverse=True)  # 무게, 용량이 큰 것부터 오도록 정렬
    trucks.sort(reverse=True)

    max_weight = 0

    j = 0
    for i in range(N):
        if weights[i] <= trucks[j]: # 화물 무게보다 트럭 적재용량이 크면
            max_weight += weights[i]# 더해주고
            j += 1                  # j += 1
                                    # 화물 무게보다 트럭 적재욕량이 작으면 다음 i로 넘어감
        if j > M-1:                 # j가 M-1보다 크면 인덱스 범위 벗어나게 됨
            break

    print(f'#{tc} {max_weight}')

