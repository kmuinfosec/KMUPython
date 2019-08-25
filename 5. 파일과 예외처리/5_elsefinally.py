# else절, finally절 이용
try:
    n = int(input("n >"))
    print(100//n)
# 다중 예외 처리 구조
# 다수의 예외 발생 시 먼저 발생한 예외의 처리 코드만 실행
except ValueError:
    print("정수를 입력하시오.")
except ZeroDivisionError:
    print("0으로 나누는 것은 불가능합니다.")
except Exception as e:
    # 지정되지 않은 모든 예외 발생 시 에러 메시지 출력
    print(e)
else:
    # 예외가 발생하지 않은 경우 실행
    print("나눗셈 연산을 수행하였습니다.")
finally:
    # try문 전체 완료 후 실행
    print("프로그램을 종료합니다.")