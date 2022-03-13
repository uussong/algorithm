import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(8)]
    words_transpose = list(zip(*words))

    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if words[i][j:j+N] == words[i][j:j+N][::-1]:
                cnt += 1
            if words_transpose[i][j:j+N] == words_transpose[i][j:j+N][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')