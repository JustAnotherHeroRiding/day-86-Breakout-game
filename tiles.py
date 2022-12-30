from turtle import Turtle
from random import *


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Tile(Turtle):
    def __init__(self,xcoords,ycoords):
        super().__init__()
        self.shape('square')
        self.color(choice(COLORS))
        self.penup()
        self.y = ycoords
        self.turtlesize(stretch_wid= 1,stretch_len= 2, outline= None)
        self.goto(xcoords, self.y)      

