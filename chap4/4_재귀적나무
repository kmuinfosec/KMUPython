import turtle


s = turtle.Screen()
t = turtle.Turtle()
angle = 30


def draw_tree(t, line_length):
    if line_length > 0:
        t.forward(line_length)
        t.left(angle)
        draw_tree(t, line_length - 10)
        t.right(angle)
        t.right(angle)
        draw_tree(t, line_length - 10)
        t.left(angle)
        t.backward(line_length)


if __name__ == "__main__":
    line_length = 60
    t.left(90)
    draw_tree(t, line_length)
