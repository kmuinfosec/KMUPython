# 시간과 관련된 기능을 가져옵니다.
import time

# n(초)를 설정합니다.
n = 10

cnt = 0
target_time = time.time() + n

while time.time() < target_time:
    cnt += 1

print("{N}초동안 {CNT}만큼 반복하였습니다.".format(N=n, CNT=cnt))
