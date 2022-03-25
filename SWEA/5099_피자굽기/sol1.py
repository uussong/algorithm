import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N: 화덕 크기, M: 피자
    Ci = [0] + list(map(int, input().split()))  # 피자 번호와 idx 맞추기 위해 [0] 앞에 넣어줌

    queue = []
    for i in range(1, N+1): # 화덕에 들어가는 피자 번호 넣어줌
        queue.append(i)

    idx = N + 1 # 화덕 크기 보다 피자가 많을 경우 그 후 들어갈 피자 번호
    pizza_num = 0

    while queue:
        pizza_num = queue.pop(0) # 1번 위치에서 피자 뺄 수 있음

        if Ci[pizza_num] // 2 != 0: # 치즈가 녹지 않았으면
            Ci[pizza_num] //= 2     # 다시 녹여주고
            queue.append(pizza_num) # 뒤에 넣어줌

        elif idx <= M:  # 더 들어갈 피자가 있다면
            queue.append(idx)   # 그 피자 번호를 넣고 
            idx += 1            # 다음 피자를 위해 idx 늘려줌

    print(f'#{tc} {pizza_num}')

