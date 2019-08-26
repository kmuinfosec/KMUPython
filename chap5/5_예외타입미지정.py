# 예외 타입 미지정
try:
    n = int(input("n >"))
    print(100//n)
except:
    print("에러가 발생하였습니다.")

# 예외 변수 이용
try:
    n = int(input("n >"))
    print(100//n)
except Exception as e:
    print("e")   # 발생한 예외의 에러 메시지 출력
