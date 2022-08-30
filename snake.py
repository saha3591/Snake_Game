from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_seg = []
        self.create_snake()
        self.head = self.all_seg[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.shape("square")
        new_segment.goto(position)
        self.all_seg.append(new_segment)

    def extend(self):
        self.add_segment(self.all_seg[-1].position())

    def move_snake(self):
        for seg in range(len(self.all_seg) - 1, 0, -1):
            x_cor = self.all_seg[seg - 1].xcor()
            y_cor = self.all_seg[seg - 1].ycor()
            self.all_seg[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
