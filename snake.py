from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
positions = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.head_position = self.head.pos()

    def create_segment(self, position):
        self.segment = Turtle(shape="square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(position)
        self.snake.append(self.segment)
        #self.segment.speed("slowest")
        #return self.segment

    def extend(self):
        self.create_segment(self.snake[-1].position())

    def create_snake(self):
        for pos in positions:
            self.create_segment(pos)

    def snake_move(self):
        # loop from the last element
        for i in range(len(self.snake) - 1, 0, -1):
            x_cor = self.snake[i - 1].xcor()
            y_cor = self.snake[i - 1].ycor()
            self.snake[i].goto(x_cor,y_cor)
        self.head.forward(DISTANCE)
        self.head_position = self.head.pos()
        return self.head_position

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)