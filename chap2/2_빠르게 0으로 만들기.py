# 빠르게 0으로 만들기
n = int(input("n="))
k = int(input("k="))

cnt = 0
while n:
    if not n % k:
        n //= k
        cnt += 1
    else:
        cnt += n % k
        n -= n % k
print("모듈이가 계산할 횟수: %d" %cnt)
