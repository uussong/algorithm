N, K = map(int, input().split())
students = [[0] * 2 for _ in range(7)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[Y][S] += 1

cnt = 0
for i in range(7):
    for j in range(2):
        # 학생이 있다면 학생수를 최대 인원수로 나눈 몫만큼 더해주고
        if students[i][j]:
            cnt += (students[i][j] // K)
            # 학생수를 최대인원수로 나눈 값의 나머지가 있을 땐 그 값에 1을 더 해줌
            if students[i][j] % K:
                cnt += 1
print(cnt)