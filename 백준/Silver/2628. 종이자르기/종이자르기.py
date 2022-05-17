width_list = [0]
height_list = [0]

width, height = map(int, input().split())
width_list.append(width)
height_list.append(height)

n = int(input())
for _ in range(n):
    direction, cut = map(int, input().split())

    if direction == 0:
        height_list.append(cut)
    else:
        width_list.append(cut)

# 가로, 세로 잘리는 위치를 오름차순 정렬해 앞뒤로 빼주면 잘린 종이 조각들의 가로 세로 길이를 구할 수 있음
# 이 때 가장 긴 가로와 세로를 구해 곱해주면 가장 큰 종이 조각의 넓이를 구할 수 있음
width_list.sort()
height_list.sort()

max_width = 0
for i in range(len(width_list)-1):
    if width_list[i+1] - width_list[i] > max_width:
        max_width = width_list[i+1] - width_list[i]

max_height = 0
for i in range(len(height_list)-1):
    if height_list[i+1] - height_list[i] > max_height:
        max_height = height_list[i+1] - height_list[i]

max_area = max_width * max_height
print(max_area)