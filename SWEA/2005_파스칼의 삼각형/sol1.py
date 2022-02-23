import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tri = [[1], [1, 1]] # DP array

    for i in range(2, N):
        tmp = [1] # 첫 번째 값은 항상 1
        for j in range(1, i):
            tmp.append(tri[i-1][j-1] + tri[i-1][j]) # 윗 줄의 수 두 개의 합을 넣기
        tmp.append(1) # 끝에 값도 항상 1
        tri.append(tmp) # 파스칼 삼각형에 누적

    print(f'#{tc}')
    for i in range(N):
        print(*tri[i])
