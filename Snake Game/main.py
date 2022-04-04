
import random
import time
import turtle
from turtle import Turtle,Screen
from snake import Snake
from food import  Food
from scoreboard import Scoreboard
screen = Screen()

screen.title("Welcome to the Snake Game!")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

is_game_on = True
screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
food = Food()
scoreboard = Scoreboard()

while is_game_on :
    screen.update()
    time.sleep(0.06)
    snake.move()
    # scoreboard.write()
    if snake.head.distance (food) < 15 :
        food.refresh()
        scoreboard.update_score()
        snake.grow()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290 or snake.collision_with_snake() is True  :
        is_game_on = False
        scoreboard.game_over()



screen.exitonclick()
