import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money = {50000: 0, 10000: 0, 5000: 0, 1000: 0, 500: 0, 100: 0, 50: 0, 10: 0}

    for key in money:
        if N // key:
            money[key] += N // key
            N -= key * money[key]

    print(f'#{tc}')
    for values in money.values():
        print(values, end=' ')
    print()
