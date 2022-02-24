from tkinter import *
from turtle import color, window_width

class Snakes:
  pass

class Foods:
  pass

GAME_WIDTH = 700
GAME_HEIGHT = 700
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BG_COLOR = "black"
SPACE_WIDTH = 50
SNAKE_SPEED = 5
SCORE = 0

def snake_turn():
  pass

def food_eat():
  pass

def game_over():
  pass

window = Tk()
window.title('Snake Game')
window.resizable(False,False) #to unabling to resize the window
score_label = Label(window,text="score: {}".format(SCORE),font=('consolas',40))
score_label.pack()

canvas = Canvas(window,bg=BG_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

#to center the window in the screen
window.update()
window_width= window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


window.mainloop()