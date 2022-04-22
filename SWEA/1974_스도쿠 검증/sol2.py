import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    rlt = 1
    for r in range(9):
        row_check = []
        col_check = []
        for c in range(9):
            if sudoku[r][c] not in row_check:
                row_check.append(sudoku[r][c])
            else:
                rlt = 0

            if sudoku[c][r] not in col_check:
                col_check.append(sudoku[c][r])
            else:
                rlt = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []  # 변수명에 숫자 먼저 오면 안 됨
            for r in range(i, i+3):
                for c in range(j, j+3):
                    if sudoku[r][c] not in check:
                        check.append(sudoku[r][c])
                    else:
                        rlt = 0


    print(f'#{tc} {rlt}')

