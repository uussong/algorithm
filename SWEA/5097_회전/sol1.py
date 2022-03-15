import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    for _ in range(M):
        num = num_list.pop(0)
        num_list.append(num)

    rlt = num_list[0]

    print(f'#{tc} {rlt}')

