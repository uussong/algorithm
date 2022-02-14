import sys

sys.stdin = open('input.txt')

# 최댓값 구하는 함수
def sum_max(lst):
    rlt = lst[0]
    for i in lst:
        if i > rlt:
            rlt = i
    return rlt

T = 10

for tc in range(1, T + 1):
    # 2차원 배열에 값 넣기
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 합을 모을 빈 리스트
    sum_list = []
    # 각 행의 합
    for r in range(len(matrix)):
        total_row = 0
        for c in range(len(matrix)):
            total_row += matrix[r][c]
        sum_list.append(total_row)

    # 각 열의 합
    for c in range(len(matrix)):
        total_col = 0
        for r in range(len(matrix)):
            total_col += matrix[r][c]
        sum_list.append(total_col)

    # 대각선의 합
    total_diagonal_1 = 0
    total_diagonal_2 = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if r == c:
                total_diagonal_1 += matrix[r][c]
            if r + c == len(matrix)-1:
                total_diagonal_2 += matrix[r][c]
    sum_list.append(total_diagonal_1)
    sum_list.append(total_diagonal_2)

    # 합이 모인 리스트의 최댓값
    ans = sum_max(sum_list)
    print(f'#{N} {ans}')

