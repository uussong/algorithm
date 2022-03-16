import sys

sys.stdin = open('input.txt')

def inorder(root):
    if root:
        inorder(int(Tree[root][1]))
        print(Tree[root][0], end='')	# 이어 적어야하기 때문에 줄바꿈 방지
        inorder(int(Tree[root][2]))

T = 10
for tc in range(1, T + 1):
    N = int(input())
    # 해당 정점의 알파벳, 왼쪽 자식, 오른쪽 자식 정정번호를 담아야하기 때문에 3칸이 필요
    Tree = [[0] * 3 for _ in range(N + 1)]

    for i in range(N):
        lst = list(input().split())
        p = int(lst[0])	# input을 문자열로 받음
        # 알파벳, 왼쪽 자식, 오른쪽 자식 정점 번호를 한 번에 가져옴
        Tree[p][0:len(lst)-1] = lst[1:len(lst)]

    print(f'#{tc} ', end ='')	# 이어 적어야하기 때문에 줄바꿈 방지
    inorder(1)
    print()	# 줄바꿈