# 가변 매개변수 함수를 정의할 때는 *를 가변 매개변수 이름 앞에 붙인다.
def get_sum(*args):
    ret = 0
    for each in args:
        ret += each
    return ret

print(get_sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
