import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8-N+1):
            row_word = ''
            for k in range(N):
                row_word += words[i][j+k]
            if row_word == row_word[::-1]:
                cnt += 1


    for i in range(8-N+1):
        for j in range(8):
            col_word= ''
            for k in range(N):
                col_word += words[i+k][j]
            if col_word == col_word[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')

