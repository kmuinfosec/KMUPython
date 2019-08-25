# 페르마의 마지막 정리 기본
for n in range(1, 5):
    print("n =", n)
    for a in range(1, 101):
        for b in range(1, 101):
            for c in range(1, 101):
                if a**n + b**n == c**n:
                    print("a: {}, b: {}, c: {}".format(a, b, c))
    else:
        print("Complete")
        print()