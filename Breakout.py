#You can try out the gameplay here:

#https://elgoog.im/breakout/


#Basically a one player reverse pong
#One line at the bottom that moves left and right
#Ball that moves constantly
#Need to detect colision with the ball
#Bunch of bricks at the top that break when the ball touches
#Every colision makes the ball reverse direction
#Continue until no more bricks
#if the ball falls down lose a life
#if no more lives gameover
#every broken brick increases the score


from turtle import *
from Paddle import Paddle
from time import sleep
from ball import Ball
from tiles import Tile
import numpy as np
from score import Score



screen= Screen()
screen.setup(width = 800,height= 600)
screen.bgcolor('black')
screen.title("Breakout")
screen.tracer(0)

player1 = Paddle((0, -250))
ball = Ball()
scoreboard = Score((350,250))
lives = Score((-350,250))
lives.update_score()

rows = []

screen.listen()
screen.onkey(player1.left,"Left")
screen.onkey(player1.right,"Right")

#Find a way to create the tiles across the screen
#Detect colision with them and delete them
#If there are no more tiles the game is over
y = 20

for x in list(np.arange(-350,350,45)):
    for y in range(20, 200, 30):
        tile = Tile(x, y)
        rows.append(tile)
game = True
while game:
    screen.update()
    sleep(ball.sleep)
    ball.move()
    for tile in rows[:]:  # Iterate over a copy of the list of tiles
        if ball.distance(tile) < 25:
            ball.bounce()
            #print("It's a hit")
            tile.ht()
            rows.remove(tile)
            scoreboard.update_score()
            if scoreboard.score % 40 == 0:
                ball.faster()
    if ball.ycor() > 280:
        ball.bounce()
    if ball.ycor() < -280:
        ball.reverse()
        ball.reset()
        lives.update_lives()
    if ball.distance(player1) < 60 and ball.ycor() < -225:
        ball.bounce()
        #print(len(rows))  
    if ball.xcor() > 380:
        ball.reverse()
        #score2.update_score()
        #score for player 2
    if ball.xcor() < -380: 
        ball.reverse()
        #score1.update_score()
        #score for player 1
    if len(rows) == 0 or lives.score == -1:
        lives.clear()
        game= False
        scoreboard.gameover()
           



screen.exitonclick()


