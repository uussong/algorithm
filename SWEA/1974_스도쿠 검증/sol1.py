import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    # 행, 열, 3x3 격자 모두에서 1부터 9까지 숫자가 하나씩 겹치지 않아야 정답
    ans = 1 # 기본값을 정답으로 둠

    # 행방향 체크
    for r in range(9):
        check = []
        for c in range(9):
            if sudoku[r][c] in check:
                ans = 0
            else:
                check.append(sudoku[r][c])
                
    # 열방향 체크
    for c in range(9):
        check = []
        for r in range(9):
            if sudoku[r][c] in check:
                ans = 0
            else:
                check.append(sudoku[r][c])

    # 3x3 격자 확인
    for i in range(0, 9, 3): # 3x3 격자이기 때문에 3칸씩 이동
        for j in range(0, 9, 3):
            check = []
            # 3x3 격자 안에서 loop
            for r in range(3):
                for c in range(3):
                    # 각 격자별로 확인해야함 - 인덱스 주의
                    if sudoku[i+r][j+c] in check:
                        ans = 0
                    else:
                        check.append(sudoku[i+r][j+c])
    print(f'#{tc} {ans}')

