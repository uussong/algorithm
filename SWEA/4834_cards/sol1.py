import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    cards = list(map(int, list(input())))


    cnt = [0]*10 # 각 숫자의 개수를 넣어줄 리스트 생성
    for card in cards:
        cnt[card] += 1

    max_num = max_cnt = 0 # 가장 많은 카드의 숫자와 장수를 넣어줄 변수 생성

    for i in range(len(cnt)):
        if cnt[i] >= max_cnt:
            max_num = i #cnt 리스트의 idx는 곧 카드의 숫자
            max_cnt = cnt[i] # cnt의 각 요소는 카드의 장수



    print(f'#{tc} {max_num} {max_cnt}')
