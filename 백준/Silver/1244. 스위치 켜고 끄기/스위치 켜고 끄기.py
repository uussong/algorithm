def change_switch(idx):
    if switch[idx] == 1:
        switch[idx] = 0
    elif switch[idx] == 0:
        switch[idx] = 1

switch_num = int(input())
switch = [-1] + list(map(int, input().split())) # 인덱스 처리를 위해 맨 앞에 0, 1 아닌 다른 값을 넣어줌
student_num = int(input())
for _ in range(student_num):
    gender, idx = map(int, input().split())

    # 남학생일 때
    if gender == 1:
        # 자기가 받은 수의 배수이면 스위치 상태 바꿈
        for i in range(idx, switch_num+1):
            if i % idx == 0:
                change_switch(i)

    # 여학생일 때
    elif gender == 2:
        # idx는 무조건 번호 바뀌게됨
        change_switch(idx)
        # 좌우 대칭 확인
        # idx를 중심으로 +-j 해줄 것이기 때문에 최대가 전체 스위치 길이의 절반이 됨
        for j in range(1, switch_num//2):
            # 범위에서 벗어난다면 break
            if idx-j < 0 or idx+j > switch_num:
                break
            # 대칭값이라면 바꿔줌
            if switch[idx-j] == switch[idx+j]:
                change_switch(idx-j)
                change_switch(idx+j)

            else:
                break

for i in range(1, switch_num+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
