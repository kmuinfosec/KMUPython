# 생일 문제
import matplotlib.pyplot as plt
import math as m
import random


# random 모듈 이용한 함수
def p_random(n, total):
    cnt = 0
    for _ in range(total):
        birth = [random.randint(1, 365) for _ in range(n)]
        if len(birth) != len(set(birth)):
            cnt += 1
    return cnt / total


# 여사건을 이용한 함수
def p(n):
    if n >= 366:
        return 1
    else:
        return 1 - m.factorial(365) / (m.factorial(365-n) * 365**n)


n_ = int(input("학생 수: "))
total_ = int(input("실행 횟수: "))
print("random 모듈을 이용해 구한 확률: {}".format(p_random(n_, total_)))
print("여사건을 이용해 구한 확률: {}".format(p(n_)))


# matplotlib 이용해 그래프 그리기
x = [i for i in range(1, 101)]
y = [p(i) for i in range(1, 101)]

plt.plot(x, y)
plt.xlabel("Number of People")
plt.ylabel("Probability")
plt.title("Birthday Problem")
plt.grid()
plt.show()
