# 구구단 출력
# for문
for i in range(1, 10):
    print("{}단".format(i))
    for j in range(1, 10):
        print("{} X {} = {}".format(i, j, i * j))
    print()

# while문
i = 1
while i < 10:
    print("{}단".format(i))
    j = 1
    while j < 10:
        print("{} X {} = {}".format(i, j, i * j))
        j += 1
    i += 1
    print()