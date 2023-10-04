## CREATE BALL CLASS

# Inherit the properties of the Turtle class
from turtle import Turtle
## Import Math module for mathematical calculation
import math
## Import Winsound module to imitate sound
import winsound

class Ball(Turtle):  

    def __init__(self,x,y):
        super().__init__()  
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.goto(x,y)
        self.step = 2
        self.velocity = [self.step,self.step]

    def move_ball(self):
        if self.ycor() <-290 or self.ycor() > 290:
            self.velocity[1] *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        new_x = self.xcor() + self.velocity[0]
        new_y = self.ycor() + self.velocity[1]
        self.goto(new_x,new_y)

    
    def bounce(self, distance, height, paddle, event):

        # Calculate ball vector length in order to keep the value after the collision
        vector_length = math.sqrt((self.velocity[0] ** 2 )+(self.velocity[1] ** 2))

        # Calculate angle based on how far from the center the ball hit the paddles
        max_angle = math.pi / 2.5  # Around 70 degrees
        relative_distance = distance / (height / 2)  # Normalize distance
        angle = abs(max_angle * relative_distance)

        # Calculate new x and y components of velocity
        new_x_velocity = math.cos(angle)*vector_length
        new_y_velocity = math.sin(angle)*vector_length
 
        # Setting the new direction of ball based on where it hits the paddles
        if event == "middle" and self.velocity[1] < 0:
            new_y_velocity *= -1
        if event == "corner" and relative_distance < 0: 
            new_y_velocity *= -1

        if paddle == "right": 
           new_x_velocity *= -1

        self.velocity[0] = new_x_velocity
        self.velocity[1] = new_y_velocity

        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        
    
               