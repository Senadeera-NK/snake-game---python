from tkinter import *
from Snake import *
from Food import *
import random
import time

def randomFood(snake):
  coordinates = snake.snakeCoordinates()
  print('first x : ', coordinates[0])
  print('second x : ', coordinates[2])

  xRandom = random.randint(0,500)
  yRandom = random.randint(0,500)
  Food(canvas,xRandom,yRandom,"blue")
 

window = Tk()
window.geometry("500x500")
window.title("Snake Game")

canvas = Canvas(window,width=500, height=500)
canvas.pack()

snake = Snake(canvas,0,0,100,10,10,0,"black")

randomFood(snake)

while True:
  snake.move()
  window.update()
  time.sleep(0.5)


window.mainloop()