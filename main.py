from tkinter import *
from Snake import *
import time

window = Tk()
window.geometry("500x500")
window.title("Snake Game")

canvas = Canvas(window,width=500, height=500)
canvas.pack()

snake = Snake(canvas,0,0,100,10,10,0,"black")

while True:
  snake.move() 
  window.update()
  time.sleep(0.5)


window.mainloop()