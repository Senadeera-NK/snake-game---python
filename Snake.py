from textwrap import fill


class Snake:
  def __init__(self,canvas,x,y,width,height,xVelocity,yVelocity,color):
    self.canvas = canvas
    self.image = canvas.create_rectangle(x,y,width,height,fill=color)
    self.xVelocity = xVelocity
    self.yVelocity = yVelocity
  
  def move(self):
      coordinates = self.canvas.coords(self.image)
     
      # if(coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
      #   self.xVelocity = -self.xVelocity
      # if(coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
      #   self.yVelocity = -self.yVelocity

      self.canvas.move(self.image,self.xVelocity,self.yVelocity)


 

