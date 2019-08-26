# 기본 사용법
import math

# math 모듈에 포함된 상수 활용
print("PI = {0}".format(math.pi))
print("자연상수 e = {0}".format(math.e))

# math 모듈에 포함된 sin/cos 함수 활용
val = math.sin(math.pi / 2)
print("sin(PI/2) = {0}".format(val))
val = math.cos(math.pi)
print("cos(PI) = {0}".format(val))


# 별칭 사용
# 모듈에 별칭(alias) 붙여 사용
import math as m

# 별칭 m으로 math 모듈의 상수 활용
print("PI = {0}".format(m.pi))
print("자연상수 e = {0}".format(m.e))

# 별칭 m으로 math 모듈의 함수 활용
val = m.sin(m.pi / 2)
print("sin(PI/2) = {0}".format(val))
val = m.cos(m.pi)
print("cos(PI) = {0}".format(val))


# from ... import ...
# 현재 네임스페이스로 모듈의 특정 함수/변수 가져오기
from math import sin
from math import pi

# math 모듈의 상수 pi를 현재 네임스페이스로 활용
print("PI = {0}".format(pi))
print("자연상수 e = {0}".format(math.e))

# math 모듈의 함수 sin()을 현재 네임스페이스로 활용
val = sin(pi / 2)
print("sin(PI/2) = {0}".format(val))
val = math.cos(pi)
print("cos(PI) = {0}".format(val))


# from ... import *
# 현재 네임스페이스로 모듈 내용 모두 가져오기
from math import *

# math 모듈의 상수를 현재 네임스페이스로 활용
print("PI = {0}".format(pi))
print("자연상수 e = {0}".format(e))

# math 모듈의 함수를 현재 네임스페이스로 활용
val = sin(pi / 2)
print("sin(PI/2) = {0}".format(val))
val = cos(pi)
print("cos(PI) = {0}".format(val))


# 문제점
e = "다섯번째 알파벳"
print(e)

from math import *

# 의도치 않게 기존 변수 e의 내용이 바뀜
# 기존의 변수 e가 math.e로 덮어씌여짐
print(e)