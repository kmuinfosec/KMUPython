import time


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

k = int(input())
start = time.time()
print("{}번째 피보나치 수열의 수: {}".format(k,fibo(k)))
print("소요된 시간: {}".format(time.time()-start))
