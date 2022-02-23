from email import message
from tkinter import *
from Snake import *
from Food import *
import time

def start():
  food = Food(canvas,"red")
  snake = Snake(canvas,0,0,10,10,10,0,"black")
  return food, snake

def AfterSnakeEatFood():
  snakeCoordinates = snake.snakeCoordinates()
  foodCoordinates = food.foodCoordinates()
  print('--------------------------------------')
  print('snake x first: ',snakeCoordinates[0])
  print('food x first: ',foodCoordinates[0])
  foodRange0 = [foodCoordinates[0],foodCoordinates[0]+1,foodCoordinates[0]+2,foodCoordinates[0]+3,foodCoordinates[0]+4,foodCoordinates[0]+5,foodCoordinates[0]+6,foodCoordinates[0]+7,foodCoordinates[0]+9,foodCoordinates[0]+10]


  if(snakeCoordinates[0] in foodRange0):
    canvas.delete(food)
    snake.growSnake()


window = Tk()
window.geometry("500x500")
window.title("Snake Game")

frame = Frame(window)
frame.pack()

canvas = Canvas(frame,width=500, height=500)
canvas.pack()

start()

while True:
  snake.move(window)
  AfterSnakeEatFood()
  window.update()
  time.sleep(0.5)

window.mainloop()