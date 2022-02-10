import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = []
    for i in range(N - M + 1):  # 숫자를 더하기 시작 할 지점을 고려
        sum_num = 0
        for j in range(M):
            sum_num += numbers[i + j]
        sum_list.append(sum_num)

    # 최댓값과 최솟값을 하드코딩 하는 대신 리스트 안의 요소로 대체
    sum_min = sum_max = sum_list[0]
    for s in sum_list:
        if s < sum_min:
            sum_min = s
        if s > sum_max:
            sum_max = s

    ans = sum_max - sum_min

    print(f'#{tc} {ans}')