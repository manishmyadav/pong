from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, LEFT_PADDLE_POSITION, RIGHT_PADDLE_POSITION, X_BOUNDARY, Y_BOUNDARY
from scoreboard import Scoreboard

screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen.tracer(0)  # Turn off the tracer animation

r_paddle = Paddle(RIGHT_PADDLE_POSITION)
l_paddle = Paddle(LEFT_PADDLE_POSITION)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='w', fun=l_paddle.go_up)
screen.onkeypress(key='s', fun=l_paddle.go_down)

screen.onkeypress(key='Up', fun=r_paddle.go_up)
screen.onkeypress(key='Down', fun=r_paddle.go_down)

game_is_on = True

# screen.tracer(1)  # Turn on the tracer i.e. animation
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if not -1*Y_BOUNDARY < ball.ycor() < Y_BOUNDARY:
        ball.bounce_y()

    # Detect collision with the paddle
    elif ball.xcor() >= 340 and ball.distance(r_paddle) <= 50 or ball.xcor() <= -340 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()

    # Detect L paddle misses
    elif ball.xcor() < -400:
        ball.reset_position()
        l_paddle.reset_position(LEFT_PADDLE_POSITION)
        r_paddle.reset_position(RIGHT_PADDLE_POSITION)
        scoreboard.r_point()

    # Detect R paddle misses
    elif ball.xcor() > 400:
        ball.reset_position()
        l_paddle.reset_position(LEFT_PADDLE_POSITION)
        r_paddle.reset_position(RIGHT_PADDLE_POSITION)
        scoreboard.l_point()

screen.exitonclick()