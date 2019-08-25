# 숫자 삼각형 1
n = int(input("n >"))
num = 1
for i in range(n):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()

# 숫자 삼각형 2
n = int(input("n >"))
for i in range(1, n + 1):
    tmp = i
    for j in range(i):
        print(tmp, end=" ")
        tmp += n - j - 1
    print()
