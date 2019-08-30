n = 10
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print(n, sum)


def sigma(n):
    if n == 1:
        return n
    else:
        return n + sigma(n - 1)


n = 10
print(n, sigma(n))
