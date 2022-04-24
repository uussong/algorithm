N = int(input())
numbers = list(map(int, input().split()))
max_v = min_v = numbers[0]

for num in numbers:
    if max_v < num:
        max_v = num

    if min_v > num:
        min_v = num

print(min_v, max_v)