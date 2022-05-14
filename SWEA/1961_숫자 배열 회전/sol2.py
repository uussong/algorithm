import sys

sys.stdin = open('input.txt')

def rotate_90(arr):
    matrix = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            matrix[c][N-r-1] = arr[r][c]

    return matrix


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    matrix = [[0] * N for _ in range(N)]

    numbers_90 = rotate_90(numbers)
    numbers_180 = rotate_90(numbers_90)
    numbers_270 = rotate_90(numbers_180)

    print(f'#{tc} ')
    for i in range(N):
        for j in range(N):
            print(numbers_90[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(numbers_180[i][j], end='')
        print(' ', end='')
        for j in range(N):
            print(numbers_270[i][j], end='')
        print('')

