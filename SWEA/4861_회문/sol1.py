import sys
from pprint import pprint

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(str, input())))
    rlt = ''

    # 가로 문자열 회문 찾기
    for r in range(N):
        # range(N-M+1): 회문이 시작되는 열 범위 지정
        for c in range(N-M+1):
            r_list = []
            for i in range(M):
                r_list.append(matrix[r][c+i])
            if r_list == r_list[::-1]:
                rlt = ''.join(r_list)

    # 세로 문자열 회문 찾기
    for c in range(N):
        # range(N-M+1): 회문이 시작되는 행 범위 지정
        for r in range(N-M+1):
            c_list = []
            for i in range(M):
                c_list.append(matrix[r+i][c])
            if c_list == c_list[::-1]:
                rlt = ''.join(c_list)

    print(f'#{tc} {rlt}')