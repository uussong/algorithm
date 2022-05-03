dwarfs = [int(input()) for _ in range(9)]
total = 0
for dwarf in dwarfs:
    total += dwarf

lier1 = lier2 = 0
for i in range(9):
    for j in range(i+1, 9):
        # 전체 합에서 거짓말쟁이 둘을 빼면 100이 나올 것
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            lier1 = dwarfs[i]
            lier2 = dwarfs[j]

real_dwarfs = []  # 거짓말 쟁이가 아닌 난쟁이만 모으기
for i in range(9):
    if dwarfs[i] != lier1 and dwarfs[i] != lier2:
        real_dwarfs.append(dwarfs[i])

real_dwarfs.sort()

for dwarf in real_dwarfs:
    print(dwarf)