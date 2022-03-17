import sys

sys.stdin = open('sample_input.txt')

def preorder(node):
    cnt = 0
    if node:
        cnt += 1
        cnt += preorder(tree[node][0])	# 모든 처리는 node에서 이루어짐
        cnt += preorder(tree[node][1])
    return cnt

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0]*2 for _ in range(E+2)]

    for i in range(0, len(edges)-1, 2):
        p = edges[i]	# 부모노드
        c = edges[i+1]	# 자식노드

        if tree[p][0] == 0:		# 왼쪽 자식이 없을 때
            tree[p][0] = c
        else:				   # 오른쪽 자식이 없을 때
            tree[p][1] = c

    print(f'#{tc} {preorder(N)}')

