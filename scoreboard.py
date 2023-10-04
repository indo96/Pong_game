## CREATE SCOREBOARD CLASS

# Inherit the properties of the Turtle class
from turtle import Turtle

class Scoreboard(Turtle):  

    def __init__(self,x,y,gamer):
        super().__init__()  
        self.penup()
        self.goto(x,y)
        self.hideturtle()
        self.point = 0
        self.gamer = gamer
        self.update_scoreboard()
          

    def update_scoreboard(self):
        self.clear()  
        self.color("white")
        self.write(f'{self.gamer}: {self.point}', align='center', font=('Courier', 24, 'normal')) 
                      
 
    def count_scores(self):
        self.point += 1
        if self.point <= 10:
            self.update_scoreboard()
        return(self.point)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"{self.gamer} wins the game!", align="center", font=("Courier", 24, "bold"))







        
 
        
