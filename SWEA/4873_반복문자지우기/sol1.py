import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    str = input()
    stack = []
    for s in str:
        # stack이 비었거나 끝자리 값과 비교하는 값이 다르면 그 값을 stack에 추가
        if len(stack) == 0 or stack[-1] != s:
            stack.append(s)
        # 아닐 경우 제거
        else:
            stack.pop()
    # 글자수를 출력해야 하므로 stack의 길이를 출력
    rlt = len(stack)
    print(f'#{tc} {rlt}')

