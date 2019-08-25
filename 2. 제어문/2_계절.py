# 계절 판별
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 봄
if 3 <= now.month <= 5:
    print("이번달은 {MONTH}월로 봄입니다.".format(MONTH=now.month))
# 여름
elif 6 <= now.month <= 8:
    print("이번달은 {MONTH}월로 여름입니다.".format(MONTH=now.month))
# 가을
elif 9 <= now.month <= 11:
    print("이번달은 {MONTH}월로 가을입니다.".format(MONTH=now.month))
# 겨울
# elif now.month == 12 or 1 <= now.month <= 2:
else:
    print("이번달은 {MONTH}월로 겨울입니다.".format(MONTH=now.month))
