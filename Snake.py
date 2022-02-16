from textwrap import fill


class Snake:
  def __init__(self,canvas,x,y,width,height,xVelocity,yVelocity,color):
    self.canvas = canvas
    self.image = canvas.create_rectangle(x,y,width,height,fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity

  def move_up(self):
    self.canvas.move(self.image,0,-10) 
  
  def move_down(self):
    self.canvas.move(self.image,0,10) 

  def move_left(self):
    self.canvas.move(self.image,0,0) 


  def move_right(self):
    pass

  def move(self,window):
    window.bind("<Up>",self.move_up)
    window.bind("<Down>",self.move_down)
    window.bind("<Left>",self.move_left)
    window.bind("<Right>",self.move_right)

    coordinates = self.canvas.coords(self.image)
    self.canvas.move(self.image,self.xVelocity,self.yVelocity)
    
  def snakeCoordinates(self):
    coordinates = self.canvas.coords(self.image)
    return coordinates
    


 

