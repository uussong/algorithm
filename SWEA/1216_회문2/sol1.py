import sys

sys.stdin = open('input.txt')

def palindrome_check(lst):
    for i in range(100, -1, -1):    # 회문의 길이를 줄여나가며 탐색
        for r in range(100):
            for c in range(100-i+1):
                if lst[r][c:c+i] == lst[r][c:c+i][::-1]:
                    return i

T = 10
for tc in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(100)]
    max_length = 0

    row_length = palindrome_check(words)
    if max_length < row_length:
        max_length = row_length

    # 행/열 바꾼 transpose
    words_transpose = list(zip(*words))
    col_length = palindrome_check(words_transpose)
    if max_length < col_length:
        max_length = col_length

    print(f'#{tc} {max_length}')