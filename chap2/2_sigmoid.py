# 활성화 함수
import math

x = int(input("x >"))

# exp(x)
exp = 0
for i in range(100):
    exp += x**i / math.factorial(i)
print(exp)

# sigmoid 함수
sigmoid = 1 / (1 + 1/exp)
print(sigmoid)