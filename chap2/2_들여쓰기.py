# 들여쓰기 기본
x = 30
y = 20
if x < y:
    print(x, "is less than", y)
    print(y, "is greater than", x)
if x > y:
    print(y, "is less than", x)
    print(x, "is greater than", y)
if x == y:
    print(x, "is equal to", y)


# 들여쓰기 등급 출력
score = int(input("100 이하의 정수 입력: "))
if 90 <= score <= 100:
    print("your score is", score, ", grade is A")
if 80 <= score < 90:
    print("your score is", score, ", grade is B")
if 70 <= score < 80:
    print("your score is", score, ", grade is C")
if 60 <= score < 70:
    print("your score is", score, ", grade is D")
if 0 <= score < 60:
    print("your score is", score, ", grade is F")



# 들여쓰기 elif 등급 출력
score = int(input("100 이하의 정수 입력: "))
if 90 <= score <= 100:
    print("your score is", score, ", grade is A")
elif 80 <= score:
    print("your score is", score, ", grade is B")
elif 70 <= score:
    print("your score is", score, ", grade is C")
elif 60 <= score:
    print("your score is", score, ", grade is D")
else:
    print("your score is", score, ", grade is F")


# 들여쓰기 한 줄 쓰기 등급 출력
score = int(input("100 이하의 정수 입력: "))
if 90 <= score <= 100: print("your score is", score, ", grade is A")
elif 80 <= score: print("your score is", score, ", grade is B")
elif 70 <= score: print("your score is", score, ", grade is C")
elif 60 <= score: print("your score is", score, ", grade is D")
else: print("your score is", score, ", grade is F")