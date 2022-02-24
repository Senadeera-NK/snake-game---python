from textwrap import fill
from Food import *


class Snake:
  def __init__(self,canvas,x,y,width,height,xVelocity,yVelocity,color):
    self.canvas = canvas
    self.image = canvas.create_rectangle(x,y,width,height,fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity

  def turn_up(self,event):
    self.xVelocity = 0
    self.yVelocity = -10
    # self.canvas.move(self.image,0,-10)
  
  def turn_down(self,event):
    self.xVelocity = 0
    self.yVelocity = 10
    # self.canvas.move(self.image,0,10) 

  def turn_left(self,event):
    self.xVelocity = -10
    self.yVelocity = 0
    # self.canvas.move(self.image,0,0) 

  def turn_right(self,event):
    self.xVelocity = 10
    self.yVelocity = 0
    # self.canvas.move(self.image,-10,0) 

  def move(self,window):
    window.bind("<Up>",self.turn_up)
    window.bind("<Down>",self.turn_down)
    window.bind("<Left>",self.turn_left)
    window.bind("<Right>",self.turn_right)

    coordinates = self.canvas.coords(self.image)
    self.canvas.move(self.image,self.xVelocity,self.yVelocity)

  def pauseSnake(self):
    self.xVelocity = 0
    self.yVelocity = 0
    print('done !!!!!!!!!!!!!!!!!!!!!!!!')
  
  def growSnake(self,snake):
    snake.coords(self.width+=10)
    print('snake grew !!!')

    
  def snakeCoordinates(self):
    coordinates = self.canvas.coords(self.image)
    return coordinates
    


 

