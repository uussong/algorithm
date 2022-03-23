import sys

sys.stdin = open('input.txt')

# 0 ~ 9까지의 수와 대응하는 이진 코드
P = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    data = ''
    for i in range(N):
        for j in range(M-1, -1, -1):    # 암호코드의 맨 뒤가 공통적으로 1이기 때문에 뒤에서 부터 탐색
            if lst[i][j] == '1':
                data += lst[i][j-55:j+1] # 코드의 총 길이 56칸이므로 한 번에 잘라줌

    codes = []
    for i in range(0, 56, 7):   # 7자리 씩 코드 자르기
        code = data[i:i+7]
        codes.append(P[code])

    # 조건에 따라 계산
    rlt = ''
    if (((codes[0]+codes[2]+codes[4]+codes[6])*3)+(codes[1]+codes[3]+codes[5])+codes[7])%10 == 0:
        rlt = sum(codes)
    else:
        rlt = 0

    print(f'#{tc} {rlt}')
