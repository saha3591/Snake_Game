from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # detect collision with food
    if snake.head.distance(food) < 13:
        food.refresh()
        # extend snake segment
        snake.extend()
        scoreboard.update_scoreboard()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.ending_message()

    # detect collision with tail
    for segment in snake.all_seg[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.ending_message()

screen.exitonclick()
