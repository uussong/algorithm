import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(5)]
    arr = [[0] * 15 for _ in range(5)]
    # board의 빈칸을 0으로 채우기 위함
    for i in range(5):
        for j in range(len(board[i])):
            arr[i][j] = board[i][j]

    word = ''
    for i in range(15): # 세로로 순회하기 때문에 행의 갯수만큼 먼저 돌아야함
        for j in range(5):
            if arr[j][i] != 0:  # 숫자 0과 문자 0이 다르기 때문에 가능
                word += arr[j][i]

    print(f'#{tc} {word}')

