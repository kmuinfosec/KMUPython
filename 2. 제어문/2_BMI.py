# 체질량 지수 계산
height = float(input("키를 입력하세요(cm): "))
weight = float(input("몸무게를 입력하세요(kg): "))
# m단위로 변환
height /= 100

BMI = weight / (height ** 2)

if BMI <= 18.5:
    print("저체중 입니다.")
elif BMI < 25:
    print("정상체중 입니다.")
elif BMI < 30:
    print("과체중 입니다.")
else:
    print("비만 입니다.")
