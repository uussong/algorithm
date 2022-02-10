import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    max_num = min_num = nums[0]

    for i in nums:
        # max_num이 i보다 작다면 i를 max_num에 할당
        if i > max_num:
            max_num = i

        # min_num이 i보다 크다면 i를 min_num에 할당
        if i < min_num:
            min_num = i

        ans = max_num - min_num

    print(f'#{tc} {ans}')