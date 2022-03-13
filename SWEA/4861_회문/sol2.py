import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    words_transpose = list(zip(*words))
    rlt = ''

    for i in range(N):
        for j in range(N-M+1):
            if words[i][j:j+N] == words[i][j:j+N][::-1]:
                rlt = ''.join(words[i][j:j+M])
            if words_transpose[i][j:j+N] == words_transpose[i][j:j+N][::-1]:
                rlt = ''.join(words_transpose[i][j:j+M])

    print(f'#{tc} {rlt}')