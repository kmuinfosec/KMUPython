import turtle
s = turtle.Screen()
# 화면중앙 (0, 0)위치에 거북이 생성
# 거북이는 오른쪽을 보고 있음.
t = turtle.Turtle()
# 100 필셀 전진
t.forward(100)
# 왼쪽으로 90도 회전. 위쪽 향함.
t.left(90)

# 두번째 거북이 생성
u = turtle.Turtle()
# 두번째 거북이 위쪽 향함.
u.left(90)
# 두번째 거북이 위로 100필셀 전진
u.forward(100)
# 첫번째 거북이 위로 100필셀 전진
t.forward(100)
# 두번째 거북이 오른쪽으로 45도 회전
u.right(45)
