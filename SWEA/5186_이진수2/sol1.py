import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    rlt = ''

    for i in range(1, 13):  # 소수점 아래 12자리 이내로만 표시하면 됨
        if N >= 0.5**i:     # N이 0.5**i보다 커야 계산 가능
            rlt += '1'
            N %= 0.5**i     # 0.5**i로 나눈 나머지가 N이됨
        else:
            rlt += '0'
        if N == 0:          # N이 0이 되면 종료
            break
    else:                   # 종료 조건을 충족하지 않았으면 13자리 이상이라는 의미
        rlt = 'overflow'

    print(f'#{tc} {rlt}')

