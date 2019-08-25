# 별 출력 6 마름모
# 1
n = int(input("n >"))
for i in range(1, n+1):
    for j in range(n - i):
        print(end=" ")
    for j in range(2*i - 1):
        print("*", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(n - i):
        print(end=" ")
    for j in range(2*i - 1):
        print("*", end="")
    print()

# 2
for i in range(1, 2*n):
    if i < n:
        for j in range(n - i):
            print(end=" ")
        for j in range(2 * i - 1):
            print("*", end="")
        print()
    else:
        i -= n
        for j in range(i):
            print(end=" ")
        for j in range(2*(n-i) - 1):
            print("*", end="")
        print()