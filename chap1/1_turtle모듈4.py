import turtle
s = turtle.Screen()
t = turtle.Turtle()
#t = turtle.Turtle(shape='turtle')
# 펜 진하게
t.pensize(3)

x = -100
y = 100
# 좌표로 선그리면서 이동
t.goto(x, y)
# 취소
t.undo()

# 그리지 않고 좌표 이동
t.penup()
t.goto(x, y)
# 그릴 준비
t.pendown()

t.dot()
# 반지름 100짜리 원 그리기.
# 거북이가 바라보는 방향의 왼쪽이 원중심.
t.circle(100)
