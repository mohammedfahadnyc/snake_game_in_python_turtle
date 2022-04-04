from turtle import Turtle, Screen


STARTING_SEGMENTS = 3
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake :

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake (self) :
        for i in range(STARTING_SEGMENTS):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(STARTING_POSITIONS[i])
            self.segments.append(segment)


    def move (self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg - 1].xcor()
            y_cor = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() !=  RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)

    def grow (self) :                       #it gets added to the position of the last segment
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        segment.goto(x_cor,y_cor)
        self.segments.append(segment)

    def collision_with_snake(self):
        for segment in self.segments[1:] :
            if self.head.distance(segment) < 10 :
                    return True
        return False


# from turtle import Turtle, Screen
#
# STARTING_SEGMENTS = 3
# STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# class Snake :
#
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
#
#     def create_snake (self) :
#         for i in range(STARTING_SEGMENTS):
#             self.add_segments()
#
#     def add_segments(self):  # it gets added to the position of the last segment
#         segment = Turtle(shape="square")
#         segment.color("white")
#         segment.penup()
#         self.segments.append(segment)
#
#     def grow (self) :
#         x_cor = self.segments[-1].xcor()
#         y_cor = self.segments[-1].ycor()        #getting x,y of the last one, then adding one to end, this is new last
#         self.add_segments()
#         self.segments[-1].goto(x_cor, y_cor)
#
#     def move (self):
#         for seg in range(len(self.segments) - 1, 0, -1):
#             x_cor = self.segments[seg - 1].xcor()
#             y_cor = self.segments[seg - 1].ycor()
#             self.segments[seg].goto(x_cor, y_cor)
#         self.head.forward(MOVE_DISTANCE)
#
#     def up(self):
#         if self.head.heading() != DOWN :
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP :
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() !=  RIGHT :
#             self.head.setheading(LEFT)
#
#     def right(self):
#         if self.head.heading() != LEFT :
#             self.head.setheading(RIGHT)
#
#
#
    # def collision_with_snake(self):
    #     for segment in self.segments[1:]:
    #         if self.head.distance(segment) < 10:
    #             return True
    #     return False
