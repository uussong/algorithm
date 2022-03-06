import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    boxes = list(map(int, input().split()))

    for i in range(n):
        # 최솟값과 최댓값을 찾고
        max_v = max(boxes)
        min_v = min(boxes)
        # 최솟값, 최댓값의 인덱스를 찾아
        max_v_index = boxes.index(max_v)
        min_v_index = boxes.index(min_v)
        # 최댓값을 -1 최솟값을 +1 해주는 걸 반복한다.
        boxes[max_v_index] -= 1
        boxes[min_v_index] += 1

    # 최종적으로 boxes의 최댓값에서 최솟값을 빼준다.
    ans = max(boxes) - min(boxes)
    print(f'#{tc} {ans}')

