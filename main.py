from email import message
from tkinter import *
from Snake import *
from Food import *
import time


def AfterSnakeEatFood():
  snakeCoordinates = snake.snakeCoordinates()
  foodCoordinates = food.foodCoordinates()
  print('--------------------------------------')
  print('snake x first: ',snakeCoordinates[0])
  print('food x first: ',foodCoordinates[0])

  foodRange0 = []
  for i in range(int(foodCoordinates[0] - 10), int(foodCoordinates[0]+10)):
    foodRange0.append(i)

  print('food Range o index: ',foodRange0)

  for foodRange in foodRange0:
    print(foodRange)
    if(foodRange == int(snakeCoordinates[0])):
      canvas.delete(food)
      snake.growSnake()

window = Tk()
window.geometry("500x500")
window.title("Snake Game")

frame = Frame(window)
frame.pack()

canvas = Canvas(frame,width=500, height=500)
canvas.pack()

food = Food(canvas,"red")
snake = Snake(canvas,0,0,10,10,10,0,"black")

while True:
  snake.move(window)
  AfterSnakeEatFood()
  window.update()
  time.sleep(0.5)

window.mainloop()