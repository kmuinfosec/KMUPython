# 별 출력 1
n = int(input("n >"))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# 별 출력 2
for i in range(1, n+1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*", end="")
    print()

# 별 출력 3
n = int(input("n >"))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 별 출력 4
n = int(input("n >"))
for i in range(n, 0, -1):
    for j in range(n - i):
        print(end=" ")
    for j in range(i):
        print("*", end="")
    print()

# 별 출력 5
n = int(input("n >"))
for i in range(1, n+1):
    for j in range(n - i):
        print(end=" ")
    for j in range(2*i - 1):
        print("*", end="")
    print()

