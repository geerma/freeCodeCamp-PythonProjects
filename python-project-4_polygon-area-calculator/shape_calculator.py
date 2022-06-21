class Rectangle:

  width = 0
  height = 0

  def __init__(self, width, height):
    self.width = width
    self.height = height
    print("Rect:",self.width,self.height)
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2*self.width + 2*self.height
    
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def get_picture(self):

    if self.height > 50 or self.width > 50:
      return "Too big for picture."

    else:
      draw = ""
      for i in range(self.height):
        for j in range(self.width):
          draw = draw + "*"
        draw = draw + "\n"
      return draw
    
  def get_amount_inside(self, Rectangle):
    number_of_times = 0

    width_remain = self.width
    height_remain = self.height

    while True:
      if height_remain >= Rectangle.height:
        if width_remain < Rectangle.width:
          break

        # Counts how many times the width of the rectangle fits
        while width_remain >= Rectangle.width:
          width_remain = width_remain - Rectangle.width
          number_of_times = number_of_times + 1

        # Reduces remaining height (goes to 'next line')
        height_remain = height_remain - Rectangle.height
        # Resets remaining width
        width_remain = self.width 
          
      else:
        break
        
    return number_of_times
  
class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side
  
  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height  
    self.width = height

  def __str__(self):
    return f"Square(side={self.width})"