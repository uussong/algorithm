import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        now = buildings[i]
        left = max(buildings[i-2:i])    # 인덱스 슬라이싱 이용
        right = max(buildings[i+1:i+3])
        
        # 현재 빌딩이 왼쪽, 오른쪽 모든 빌딩보다 높아야 조망권 확보
        if now > left and now > right:
            ans += now - max(left, right)

    print(f'#{tc} {ans}')

