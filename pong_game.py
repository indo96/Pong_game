#### CREATE PONG GAME ###############################################################
#####################################################################################

#### IMPORT NEEDED MODULES

## Turtle module to create the basics of the game
from turtle import Turtle, Screen 

## Paddle Class to create paddle individual
from paddle import Paddle

## Ball Class to create ball individual
from ball import Ball

## Scoreboard Class to create ball individual
from scoreboard import Scoreboard

## Keyboard module for flexible usage of keyboards
import keyboard

## Time module for flexible setting of time 
import time  

## Random module to reset paddles and ball
import random

## Import Math module for mathematical calculation
import math


###########################################################

#### SETTINGS

## Screen
main_screen = Screen()
main_screen.title("Pong")
main_screen.bgcolor("grey10")
main_screen.setup(800,600)
main_screen.tracer(0)  

## Net
net_drawer = Turtle()
net_drawer.penup()
net_drawer.goto(0,-290) 
net_drawer.left(90)
net_drawer.color("white")
net_drawer.pensize(3)


for i in range(10):
    net_drawer.pendown()
    net_drawer.forward(30)
    net_drawer.penup()
    net_drawer.forward(30)

net_drawer.hideturtle()    

## Paddles
l_paddle = Paddle(-370,0)
r_paddle = Paddle(370,0)
# Parameters of paddles
paddle_height = 125
paddle_width = 25
paddle_dist = math.sqrt((paddle_height/2) ** 2 + (paddle_width/2) ** 2)

## Ball
ball = Ball(0,0)



## Scoreboard
l_scoreboard = Scoreboard(-150,250,"Player L")
r_scoreboard = Scoreboard(150,250,"Player R")


##############################################################

def reset_game():

    # Generate random velocity values within the range [-3, 3]
    x_velocity = random.choice([-4, -3, 3, 4])
    y_velocity = random.choice([-4, -3, 3, 4])
    ball.velocity = [x_velocity, y_velocity]

    ball.goto(0, 0)
    l_paddle.goto(-370, 0)
    r_paddle.goto(370, 0)


###############################################################

#### GAME
# Initialize the scores for both players
r_score = 0
l_score = 0
game_is_on = True

while game_is_on:
    
    # With Time module the game can be slower
    time.sleep(0.01) 

    # Screen update after every changes 
    main_screen.update()

    # Usage of move_ball function for ball movement
    ball.move_ball()

    # With Keyboard module pressing buttons makes movements continuous
    if keyboard.is_pressed('Up'):
        r_paddle.move_up()
    if keyboard.is_pressed('Down'):  
        r_paddle.move_down()
    if keyboard.is_pressed('w'): 
        l_paddle.move_up()
    if keyboard.is_pressed('s'):
        l_paddle.move_down()
    if keyboard.is_pressed('r'): # Restart everytime pressing 'r'
        reset_game()          

    # In case of collision of ball and paddle
    # Left paddle
    if (ball.xcor() < -350 and ball.xcor() > -370) and abs(l_paddle.ycor()-ball.ycor()) < (paddle_dist): 
        ball.setx(-350)

        ball_paddle_dist = ball.ycor()-l_paddle.ycor()

        if (abs(ball_paddle_dist) > ((5*paddle_height/2)/6)):
            ball.bounce(ball_paddle_dist, paddle_height,"left","corner")
        else:
            ball.bounce(ball_paddle_dist, paddle_height,"left","middle")
    # Right paddle
    if (ball.xcor() > 350 and ball.xcor() < 370) and abs(r_paddle.ycor() - ball.ycor()) < (paddle_dist):
        ball.setx(350)

        ball_paddle_dist = ball.ycor() - r_paddle.ycor()

        if (abs(ball_paddle_dist) > ((5*paddle_height/2)/6)):
            ball.bounce(ball_paddle_dist, paddle_height,"right","corner")
        else:
            ball.bounce(ball_paddle_dist, paddle_height,"right","middle")      
        

    # In case of ball leaving the table - one of the players gaining score
    if ball.xcor() <= -390:
        r_score = r_scoreboard.count_scores()
        reset_game()    

    if ball.xcor() >= 390:
        l_score = l_scoreboard.count_scores()
        reset_game() 

    # One of the players wins the game (reaching 10 scores)
    # Right player wins
    if r_score == 10:
        net_drawer.clear()
        ball.step = 0
        ball.hideturtle()
        r_scoreboard.gameover() 
        main_screen.update() 
        time.sleep(2)
        game_is_on = False #break # Game over  

    # Left player win
    if l_score == 10:
        net_drawer.clear()
        ball.step = 0
        ball.hideturtle()
        l_scoreboard.gameover() 
        main_screen.update()
        time.sleep(2)
        game_is_on = False #break # Game over 
               
     
    

        
    



