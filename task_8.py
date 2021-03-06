import turtle
import time


def draw_cube_spiral(size, scale=40, coef=0):
    for i in range(size):
        for j in range(10, scale + 1, 10):
            turtle.forward(5 + j + coef)
            turtle.left(90)

        coef += scale


if __name__ == '__main__':
    turtle.shape('turtle')
    time.sleep(1)

    draw_cube_spiral(10)
    time.sleep(1)
