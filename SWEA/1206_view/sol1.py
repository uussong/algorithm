# min 활용

import sys

sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    view = 0

    for i in range(2, N-2):
        if buildings[i]-buildings[i-2] > 0 and buildings[i]-buildings[i-1] > 0 and buildings[i]-buildings[i+1] > 0 and buildings[i]-buildings[i+2] > 0:
            view += min(buildings[i]-buildings[i-1], buildings[i]-buildings[i-2], buildings[i]-buildings[i+1], buildings[i]-buildings[i+2])

    print(f'#{t} {view}')