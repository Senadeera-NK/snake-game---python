from ast import Lambda
import random
from tkinter import *
from django.test import tag


GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100 #how will the canvas update(snake's speed)
SPACE_SIZE = 25
BODY_PARTS = 3 #how many body parts does the snake has in the begining of the game
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class Snakes:
  def __init__(self):
    self.body_size = BODY_PARTS 
    self.coordinates = []
    self.squares = []

    for i in range(0, BODY_PARTS):
      self.coordinates.append([0,0])
    
    for x,y in self.coordinates:
      square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill = SNAKE_COLOR,tag = "snake")
      self.squares.append(square)

class Foods:
  def __init__(self):
    x = random.randint(0,(GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
    y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

    self.coordinates = [x,y]

    canvas.create_oval(x,y,x + SPACE_SIZE,y + SPACE_SIZE, fill = FOOD_COLOR, tag= "food")


def next_turn(snake,food):
  x,y = snake.coordinates[0]

  if direction == "up":
    y -= SPACE_SIZE
  elif direction == "down":
    y += SPACE_SIZE
  elif direction == "left":
    x -= SPACE_SIZE
  elif direction == "right":
    x += SPACE_SIZE

  snake.coordinates.insert(0,(x,y))
  square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
  snake.squares.insert(0,square)

  if x == food.coordinates[0] and y == food.coordinates[0]:
    global score
    score += 1
    score_label.config(text = "Score: {}".format(score))
    canvas.delete("food") #using the name of the tag to delete the object
    food = Foods() #another new food

    #only delete the last part of the body if we didn't eat the food
  else:
    del snake.coordinates[-1] #last square deletes
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]
  
  if check_collisions(snake):
    game_over()
  else:
    window.after(SPEED,next_turn,snake,food)



def change_direction(new_direction):
  global direction #the one that defined before

  if new_direction == 'left':
    if direction != 'right':
      direction = new_direction
  elif new_direction == 'right':
    if direction != 'left':
      direction = new_direction
  elif new_direction == 'up':
    if direction != 'down':
      direction = new_direction
  if new_direction == 'down':
    if direction != 'up':
      direction = new_direction

def check_collisions(snake):
  x,y = snake.coordinates[0]

  if x<0 or x>= GAME_WIDTH:
    return True
  elif y<0 or y>= GAME_HEIGHT:
    return True

  #what if snake touches it's body 
  for body_part in snake.coordinates[1:]: #everything after the head
    if x == body_part[0] and y == body_part[1]:
      print('GAME OVER')
      return True

  return False



def game_over():
  canvas.delete(ALL)
  canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70), text="GAME OVER", fill = "red", tag = "game over")

window = Tk()
window.title("Snake Game")

#to unabling to resize the window
window.resizable(False,False)

score = 0
direction = 'down' 

score_label = Label(window,text="score: {}".format(score),font=('consolas',40))
score_label.pack()

canvas = Canvas(window,bg=BACKGROUND_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvas.pack()

#to center the window in the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#how much adjusting the position
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window.bind('<Left>', lambda event : change_direction('left'))
window.bind('<Right>', lambda event : change_direction('right'))
window.bind('<Up>', lambda event : change_direction('up'))
window.bind('<Down>', lambda event : change_direction('down'))


snake = Snakes()
food = Foods()

next_turn(snake,food)

window.mainloop()