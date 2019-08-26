def hanoi(n, start, mid, end):
    # 원판이 1개인 경우 바로 옮길 수 있다.
    if n == 1:
        print("%d : %c -> %c" %(n, start, end))
    else:
        # n-1개의 원판을 start에서 mid로 먼저 옮겨준다.
        hanoi(n - 1, start, end, mid)
        # 가장 아래에 있던 n번째 원판을 start에서 end로 옮겨준다.
        print("%d : %c -> %c" %(n, start, end))
        # mid에 있는 n-1개의 원판을 end로 옮겨준다.
        hanoi(n-1, mid, start, end)


if __name__ == "__main__":
    n = int(input("N : "))
    hanoi(n, "A", "B", "C")
