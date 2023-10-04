## CREATE PADDLE CLASS

# Inherit the properties of the Turtle class
from turtle import Turtle

class Paddle(Turtle):  

    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(x,y)
        self.step = 10

    def move_up(self):
        # Handling the top side:
        if self.ycor() <= 230:
            new_y = self.ycor() + self.step
            self.goto(self.xcor(),new_y)
    
    def move_down(self):
        # Handling the bottom side:
        if self.ycor() >= -230:
            new_y = self.ycor() - self.step
            self.goto(self.xcor(),new_y)





