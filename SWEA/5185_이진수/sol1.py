import sys

sys.stdin = open('sample_input.txt')
# 16진수에 대응하는 2진수 딕셔너리
P = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
T = int(input())
for tc in range(1, T + 1):
    N, number = input().split()
    rlt = ''
    for num in number:  # input으로 받은 number를 한 글자씩 딕셔너리와 대응시켜줌
        num = P[num]
        rlt += num

    print(f'#{tc} {rlt}')