# 예외 타입 지정
try:
    n = int(input("n >"))
    print(100//n)
except ValueError:
    print("정수를 입력하시오.")
except ZeroDivisionError:
    print("0으로 나누는 것은 불가능합니다.")

# 예외 변수 이용
try:
    n = int(input("n >"))
    print(100//n)
except ValueError as e1:
    print(e1)   # 에러 메시지 출력
except ZeroDivisionError as e2:
    print(e2)   # 에러 메시지 출력