import sys

sys.stdin = open('sample_input.txt')

def check_bracket(str):
    bracket = [] # 괄호를 담을 stack
    for s in str:
        # 여는 괄호인 경우 bracket에 넣어준다.
        if s == '(' or s == '{':
            bracket.append(s)
        # ')'일 경우와 '}'인 경우를 분리해서 생각
        elif s == ')':
            # 닫는 괄호인데 bracket에 아무것도 없을 경우 짝을 이루지 못한 것
            if len(bracket) == 0:
                return 0
            # bracket에 맨 위값이 '('가 아닌 경우도 짝이 아님
            elif bracket.pop() != '(':
                return 0
        elif s == '}':
            # 닫는 괄호인데 bracket에 아무것도 없을 경우 짝을 이루지 못한 것
            if len(bracket) == 0:
                return 0
            # bracket에 맨 위값이 '{'가 아닌 경우도 짝이 아님
            elif bracket.pop() != '{':
                return 0
    # 끝가지 검사했는데 bracket의 아무 것도 없는 경우는 모두 짝이 맞은 것
    if len(bracket) == 0:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    str = input()
    rlt = check_bracket(str)
    print(f'#{tc} {rlt}')

