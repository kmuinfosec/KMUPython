a = [0.1]
s = sum(a * 10)

if s == 1:
    print('s = 1')
else:
    print('s != 1')

EPS = 0.0000001 # 최대 오차범위
if abs(s - 1) <= EPS:
    print('s = 1')
else:
    print('s != 1')
