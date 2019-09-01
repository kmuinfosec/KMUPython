# 삼각형 판별
a = int(input("a> "))
b = int(input("b> "))
c = int(input("c> "))
if a ** 2 + b ** 2 == c ** 2:
    print("직각 삼각형 입니다.")
elif a ** 2 + b ** 2 > c ** 2:
    print("예각 삼각형 입니다.")
else:
    print("둔각 삼각형 입니다.")
