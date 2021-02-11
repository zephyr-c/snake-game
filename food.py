from turtle import Turtle

import random

def random_color():
    r = random.randint(30, 255)
    g = random.randint(30, 255)
    b = random.randint(30, 255)

    return (r, g, b)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random_color())
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.color(random_color())
        self.goto(rand_x, rand_y)