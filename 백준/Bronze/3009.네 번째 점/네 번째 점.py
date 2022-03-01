x_lst = []
y_lst = []
for _ in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

for i in x_lst:
    if x_lst.count(i) == 1:
        x_rlt = i
for i in y_lst:
    if y_lst.count(i) == 1:
        y_rlt = i

print(x_rlt, y_rlt)