import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    postfix = input().split()
    stack = []

    for token in postfix:
        # 숫자라면 stack에 int로 형변환해 넣는다.
        if token.isdecimal():
            stack.append(int(token))

        else: # 연산자라면
            # .가 나올 때 길이가 1이면 pop해서 결과값에 할당 아니라면 error
            if token == '.':
                if len(stack) == 1:
                    ans = stack.pop()
                else:
                    ans = 'error'
                break
            # stack의 길이가 두 개가 안 되면 숫자가 2개가 안 된단 말이니 연산 불가 error
            elif len(stack) < 2:
                ans = 'error'
                break
            # 먼저 pop한 숫자를 뒤에 놓고 연산 해줘야 함
            num2 = stack.pop()
            num1 = stack.pop()
            if token == "+":
                rlt = num1 + num2
                stack.append(rlt)
            elif token == "-":
                rlt = num1 - num2
                stack.append(rlt)
            elif token == "*":
                rlt = num1 * num2
                stack.append(rlt)
            elif token == "/":
                rlt = num1 // num2
                stack.append(rlt)
    print(f'#{tc} {ans}')

