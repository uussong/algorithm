import sys

sys.stdin = open('input.txt', encoding='utf-8')

def count_pattern(pattern, text):
    cnt = 0

    for i in range(len(text)):
        if text[i] == pattern[0]:
            if text[i:i + len(pattern)] == pattern:
                cnt += 1
    return cnt

T = 10

for tc in range(1, T + 1):
    n = int(input())
    pattern = input()
    text = input()

    rlt = count_pattern(pattern, text)
    print(f'#{tc} {rlt}')

