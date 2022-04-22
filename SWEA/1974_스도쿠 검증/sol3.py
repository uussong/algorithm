import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    rlt = 1
    for r in range(9):
        row_check = [0]*10
        col_check = [0]*10
        for c in range(9):
            if row_check[sudoku[r][c]]:
                rlt = 0
            else:
                row_check[sudoku[r][c]] = 1

            if col_check[sudoku[c][r]]:
                rlt = 0
            else:
                col_check[sudoku[c][r]] = 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_check = [0]*10
            for r in range(i, i+3):
                for c in range(i, i+3):
                    if block_check[sudoku[r][c]]:
                        rlt = 0
                    else:
                        block_check[sudoku[r][c]] = 1

    print(f'#{tc} {rlt}')

