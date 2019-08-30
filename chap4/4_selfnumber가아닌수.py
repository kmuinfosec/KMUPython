MAXN = 1000

n = int(input())
ans = []

def d(num):
    ret = num
    while num:
        ret += num % 10
        num //= 10

    if ret > MAXN:
        return
    ans.append(ret)
    d(ret)
d(n)
for i in ans:
    print(i)
