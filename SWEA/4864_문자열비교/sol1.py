import sys

sys.stdin = open('sample_input.txt')

def count_pattern(pattern, text):
    cnt = 0

    for i in range(len(text)):
        # 첫 글자 비교
        if text[i] == pattern[0]:
            # 첫 글자가 같다면 pattern만큼 잘라서 같은지 비교
            if text[i:i + len(pattern)] == pattern:
                # cnt에 1 추가
                cnt += 1
    return cnt

T = int(input())

for tc in range(1, T + 1):
    pattern = input()
    text = input()

    rlt = count_pattern(pattern, text)
    print(f'#{tc} {rlt}')