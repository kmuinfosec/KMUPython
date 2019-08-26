# 조화급수와 로그 기본
# n = 100
import math

h_n = 0
for i in range(1, 101):
    h_n += 1/i
print("n = 100일 때 조화급수 값:", h_n)
print("ln 101:", math.log(101))
print("오차:", h_n - math.log(101))