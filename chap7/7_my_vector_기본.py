# my_vector
class Vec2:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        msg = "(" + str(self.x) + "," + str(self.y) + ")"
        return msg

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)


# Vec2 클래스 테스트
p = Vec2(3, 4)
q = Vec2(-1, 2)
r = p + q
print(p)
print(q)
print(r)