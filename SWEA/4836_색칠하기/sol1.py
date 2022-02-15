import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 10x10 영역
    area = [[0 for _ in range(10)] for _ in range(10)]
    # 각 사각형의 좌표, 색상
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 사각형 영역에 color 값 부여
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                area[r][c] += color # =color로 주면 색이 덮어씌어짐

    # 보라색 칸 판별 (빨강(1)+파랑(2)=보라(3))
    cnt = 0
    for r in range(10):
        for c in range(10):
            if area[r][c] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

