# 피보나치 수열을 구하는 함수
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

n = int(input("n >"))
print("{}번째 피보나치 수 : {}".format(n, fibo(n)))
