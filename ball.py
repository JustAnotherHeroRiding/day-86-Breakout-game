from turtle import *
from time import sleep
UPLEFT = 135
DOWNRIGHT = 315
DOWNLEFT = 225
UPRIGHT = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        #self.northwall = False Cool attempt but much more long winded
        self.x_move = -10
        self.y_move = -10
        self.sleep = 0.06
    def move(self):
        """ if self.northwall:
            newx = self.xcor() + self.x_move
            newy = self.ycor() - 10
            self.goto(newx, newy)
        else:             """
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx, newy)
        """if self.ycor() > 280:
        elf.northwall = True """         # the angela way is much simpler
    def bounce(self):
        self.y_move *= -1
    def reverse(self):
        self.x_move *= -1
    def reset(self):
        self.goto(0, 0)
        self.reverse()
        self.x_move = -10
        self.y_move = -10
        self.sleep = 0.06
    def faster(self):
        #self.x_move = self.x_move + 5
        #self.y_move = self.y_move + 5   
        self.sleep = (self.sleep * 0.8) 