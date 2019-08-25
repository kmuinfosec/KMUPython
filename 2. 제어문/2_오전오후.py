# 오전 / 오후 판별
import datetime

# 현재 날짜 /시간을 구합니다.
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
    print("현재 시간은 {HOUR}시로 오전입니다.".format(HOUR=now.hour))
else:
    print("현재 시간은 {HOUR}시로 오후입니다.".format(HOUR=now.hour))