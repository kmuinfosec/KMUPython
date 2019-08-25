# 요일 구하기
year = int(input("Enter the year = "))
month = int(input("Enter the month = "))
day = int(input("Enter the day = "))
days = 0

# year
for i in range(1, year):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        days += 366
    else:
        days += 365

# month
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(month - 1):
    days += m[i]
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    days += 1

# day
days += day

# 요일 출력
week_days = ["일", "월", "화", "수", "목", "금", "토"]
print("{Y}년 {M}월 {D}일은 {W}요일 입니다.".format(Y=year, M=month, D=day, W=week_days[days % 7]))

