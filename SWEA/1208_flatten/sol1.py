import sys

sys.stdin = open('input.txt')


# boxes 정렬 함수
# counting sort
def sort_box(boxes):
    cnt = [0] * (len(boxes) + 1)
    rlt = [0] * len(boxes)

    for box in range(len(boxes)):
        cnt[boxes[box]] += 1

    # 누적합
    for box in range(1, len(cnt)):
        cnt[box] += cnt[box - 1]

    # 정렬된 결과 저장
    for box in range(len(rlt) - 1, -1, -1):
        cnt[boxes[box]] -= 1
        rlt[cnt[boxes[box]]] = boxes[box]

    return rlt

T = 10

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 최솟값 += 1 최댓값 -=1를 덤프 횟수만큼 반복
    for i in range(N):
        boxes[-1] -= 1
        boxes[0] += 1
        boxes = sort_box(boxes)

    ans = boxes[-1] - boxes[0]
    print(f'#{tc} {ans}')
