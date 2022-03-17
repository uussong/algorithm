import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split()) # 노드의 개수, 리프 노드의 개수, 출력할 노드번호
    tree = [0] * (N+1)

    for _ in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    # 리프노드에서 부터 더하기 시작
    # i//2번의 노드에 i노드의 값이 더해짐
    for i in range(N, 1, -1):
        tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')










    #
    # N, M, L = map(int, input().split())
    # tree = [0] * (N+1)
    #
    # for _ in range(M):
    #     leaf, value = map(int, input().split())
    #     tree[leaf] = value
    #
    # for i in range(N, 1, -1):
    #     tree[i//2] += tree[i]
    #
    # print(f'#{tc} {tree[L]}')

