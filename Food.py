class Food:

  def __init__(self,canvas,x,y,color):
    self.canvas = canvas
    self.x = x
    self.y = y
    self.color = color
    canvas.create_rectangle(x,y,x + 10 ,y + 10 ,fill=color)
