import turtle as t
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DEFAULT_COLOR = ("lime")
t.colormode(255)


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('circle')
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position, color=DEFAULT_COLOR):
        body_segment = t.Turtle(shape='square')
        body_segment.color(color)
        body_segment.pu()
        body_segment.setpos(position)
        self.segments.append(body_segment)

    def extend_snake(self, color=DEFAULT_COLOR):
        self.add_segment(self.tail.position(), color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        self.__init__()