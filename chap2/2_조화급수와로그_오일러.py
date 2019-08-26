# 조화급수와 로그 오일러 상수
# n = [1...100]
for i in range(1, 101):
    h_n = 0
    for j in range(1, i + 1):
        h_n += 1 / j
    print("n = {}일 때 조화급수 값: {}".format(i, h_n))
    print("ln {}: {}".format(i+1, math.log(i + 1)))
    print("오차: ", h_n - math.log(i + 1))
    print()