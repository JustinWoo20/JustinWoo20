from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
# left paddle movement
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
#right paddle movement
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    # Detect collisions with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.wall_bounce()
    # Detect collisions with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
    # Detect collisions with  left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
    # Detect if the player missed the ball
    if ball.xcor() >= 380:
        ball.new_ball()
        score.l_get_point()
    if ball.xcor() <= -380:
        ball.new_ball()
        score.r_get_point()

    # Finish the game
    if score.r_score == 10:
        game_is_on = False
        score.r_winner()
    if score.l_score == 10:
        game_is_on = False
        score.r_winner()








screen.exitonclick()