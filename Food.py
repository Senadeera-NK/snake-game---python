import random
from Snake import *

class Food:

  def __init__(self,canvas,color):
    self.canvas = canvas
    x = random.randint(0,500)
    y = random.randint(0,500)
    self.color = color
    self.image = canvas.create_rectangle(x,y,x + 10 ,y + 10 ,fill=color)

  # def randomFood(canvas):
  #   xRandom = random.randint(0,500)
  #   yRandom = random.randint(0,500)
  #   food = Food(canvas,xRandom,yRandom,"blue")
  #   return food

  def foodCoordinates(self):
    coordinates = self.canvas.coords(self.image)
    return coordinates
    