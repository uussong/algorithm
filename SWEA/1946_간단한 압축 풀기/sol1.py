import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    unzip = ''
    rlt = ''
    for _ in range(N):
        Ci, Ki = input().split()
        Ki = int(Ki)
        unzip += Ci*Ki

    print(f'#{tc}')

    cnt = 0
    for i in unzip:
        print(i, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()

