import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    n = int(input())
    boxes = list(map(int, input().split()))

    for i in range(n):
        max_v = max(boxes)
        min_v = min(boxes)
        max_v_index = boxes.index(max_v)
        min_v_index = boxes.index(min_v)
        boxes[max_v_index] -= 1
        boxes[min_v_index] += 1

    ans = max(boxes) - min(boxes)
    print(f'#{tc} {ans}')

