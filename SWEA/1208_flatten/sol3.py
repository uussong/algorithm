import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    ans = 0

    while dump > 0:
        max_v = min_v = boxes[0]
        max_v_idx = min_v_idx = 0
        
        # enumerate 사용해 최대, 최소값의 인덱스도 함께 구해줌
        for idx, box in enumerate(boxes):
            if max_v < box:
                max_v = box
                max_v_idx = idx
            elif min_v > box:
                min_v = box
                min_v_idx = idx

        boxes[max_v_idx] -= 1
        boxes[min_v_idx] += 1

        dump -= 1
    
    # 덤프 후 최대, 최소값 구하기 위해 다시 한 번 초기화
    max_v = min_v = boxes[0]
    max_v_idx = min_v_idx = 0

    for box in boxes:
        if max_v < box:
            max_v = box
        elif min_v > box:
            min_v = box

    ans = max_v - min_v

    print(f'#{tc} {ans}')

