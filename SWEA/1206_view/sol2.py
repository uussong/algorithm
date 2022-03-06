import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    view = 0

    for i in range(2, N-1):
        if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            view += min(buildings[i]-buildings[i-1], buildings[i]-buildings[i-2], buildings[i]-buildings[i+1], buildings[i]-buildings[i+2])
    print(f'#{tc} {view}')

