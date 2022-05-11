N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 4 3 2 1 순으로 갯수를 센 리스트를 만듦
    a = [0] * 4
    b = [0] * 4
    for i in A[1:]:
        a[4-i] += 1
    for i in B[1:]:
        b[4-i] += 1

    # 각각의 갯수마다 승부 기록을 담음
    score = []
    for i in range(4):
        if a[i] > b[i]:
            score.append('A')
        elif a[i] < b[i]:
            score.append('B')
        else:
            score.append('D')

    # 앞에서(4부터) 부터 크기 비교
    draw_cnt = 0
    for i in range(4):
        if score[i] == 'A':
            print('A')
            break
        elif score[i] == 'B':
            print('B')
            break
        # 처음부터 끝까지 무승부면 무승부
        elif score[i] == 'D':
            draw_cnt += 1
            if draw_cnt == 4:
                print('D')
