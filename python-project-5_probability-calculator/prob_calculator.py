import copy
import random

class Hat:

  def __init__(self, **balls):
    #print("Balls: ",balls) - **balls in the form of: { 'color': number }

    self.contents = []
    
    for ball in balls:
      #print(ball) - Prints ball color
      #print(balls[ball]) - Prints number of balls of that color
      for number in range(balls[ball]):
        self.contents.append(ball)
    
    print(self.contents)

  def draw(self,number):

    #print("Old contents: ",self.contents)
    #print("length: ",len(self.contents))

    self.removed_balls = [] # List of removed balls
    
    for loops in range(number):
      #print("length: ",len(self.contents)) 
      if len(self.contents) == 0:
        break
      else:
        random_number = random.randint(0, (len(self.contents)-1)) # Random int from 0 to last index
        # Remove a random ball and append it to the list 'removed_balls'
        ball_taken = self.contents.pop(random_number)
        self.removed_balls.append(ball_taken)
    
    #print("New contents: ",self.contents)
    #print("Removed balls: ",self.removed_balls)
    
    return self.removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  print("")
  print("hat contents: ", hat.contents)
  print("expected: ",expected_balls)
  print("num to be drawn: ",num_balls_drawn)
  
  N = num_experiments # number of experiments
  M = 0 # number of times we get result

  color_list = [] # List of strings of expected colors
  number_list = [] # List of amount of expected balls, same index as color
  for color in expected_balls:
    #print(color, expected_balls[color])
    color_list.append(color)
    number_list.append(expected_balls[color])
    
  length = len(expected_balls) # Length of the list of expected balls
  #print("length: ",len(expected_balls))
  #print(color_list)
  #print(number_list)
  
  for experiments in range(num_experiments):
    experimental_hat = copy.deepcopy(hat)
    experimental_removed = experimental_hat.draw(num_balls_drawn)

    # Conditionals depending on length of expected_balls.
    # This alternative is used, since there is a variable number of colors in expected_balls
    # Below code is for expected balls having only 2 or 3 colors 
    # Depending on length, check if the amount of balls in experimental_removed (actually removed) 
    #   is greater than the amount of balls in number_list (expected to be removed) for each color
    # If True, increment M (number of times result occured)
    # Improvements for code could be made by making if-statements dynamic (depends on how many colors of expected balls)
    if length == 2:
      if experimental_removed.count(color_list[0]) >= number_list[0] and experimental_removed.count(color_list[1]) >= number_list[1]:
        M = M + 1
    elif length == 3:
      #print(color_list[0], color_list[1], color_list[2])
      if experimental_removed.count(color_list[0]) >= number_list[0] and experimental_removed.count(color_list[1]) >= number_list[1] and experimental_removed.count(color_list[2]) >= number_list[2]:
        M = M + 1
      
  print("number of experiments: ", N)
  print("number of times results occured: ", M)

  probability = M / N # Probability is left as fractional percentage

  print("Probability: ", probability)
  return probability