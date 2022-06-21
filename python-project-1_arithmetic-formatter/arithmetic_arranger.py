def arithmetic_arranger(problems, display = False):
    
  # Error Checking: Limit of 5 elements/problems
  if len(problems) > 5:
    return "Error: Too many problems."
  
  # Error Checking: Operands should only contain digits
  if any(character.isalpha() for problem in problems for character in problem):
    return "Error: Numbers must only contain digits."

  first_list = [] # Will be used for the top operand string
  second_list = [] # Will be used for the bottom operand string
  operator_list = [] # List of all operators
  split_problem_list = [] # Splitting the string at operator to leave numbers by themselves
  for problem in problems:
    problem = problem.replace(" ", "") # Remove whitespaces
    #print("split: ",problem)
    if '+' in problem:
      operator = "+"
      split_problem_list = problem.split("+")
    elif '-' in problem:
      operator = "-"
      split_problem_list = problem.split("-")
    # Error Checking: Only + or - operators
    elif '*' in problem or '/' in problem:
      return "Error: Operator must be '+' or '-'."

    print(problem)
    print("split problem list: ",split_problem_list)
    print("test: ",split_problem_list[1])
    first_list.append(split_problem_list[0])
    second_list.append(split_problem_list[1])
    operator_list.append(operator)

  top_string = "" # String for all top operands
  bottom_string = "" # String for all bottom operands and operators
  dash_string = "" # String for dashes
  answer_string = "" # String for (optional) answers
  # Looping through all numbers
  # .rjust() will depend on the length of the largest number, which is max_rjust
  # Will 
  for x in range(0,len(first_list)):
    max_rjust = max(first_list[x], second_list[x], key=len)
    max_rjust = int(len(max_rjust))
    # Error Checking: Operand has a max of 4 digits
    if max_rjust > 4:
      return "Error: Numbers cannot be more than four digits."

    if x == 0: # If first number (most left-hand side)
      top_string = top_string + "  " + first_list[x].rjust(max_rjust)
      bottom_string = bottom_string + operator_list[x] + " " + second_list[x].rjust(max_rjust)
      dash_string = dash_string + "--" + str(max_rjust*"-")

      # For answer string:
      if operator_list[x] == "+":
        answer = int(first_list[x]) + int(second_list[x]) # Addition case
      else:
        answer = int(first_list[x]) - int(second_list[x]) # Subtraction case
      answer_rjust = len(str(answer)) # .rjust() will also depend on digits of answer
      if answer_rjust > max_rjust:
        answer_string = answer_string + " " + str(answer).rjust(answer_rjust)
      else:
        answer_string = answer_string + "  " + str(answer).rjust(answer_rjust)

    else: # If not the first number
      top_string = top_string + "      " + first_list[x].rjust(max_rjust)
      bottom_string = bottom_string +  "    " + operator_list[x] + " "+ second_list[x].rjust(max_rjust)
      dash_string = dash_string + "    " + "--" + str(max_rjust*"-")

      # For answer string:
      if operator_list[x] == "+":
        answer = int(first_list[x]) + int(second_list[x]) # Addition case
      else:
        answer = int(first_list[x]) - int(second_list[x]) # Subtraction case
      answer_rjust = len(str(answer)) # .rjust() will also depend on digits of answer
      if answer_rjust > max_rjust:
        answer_string = answer_string + "     " + str(answer).rjust(answer_rjust)
      else:
        answer_string = answer_string + "      " + str(answer).rjust(answer_rjust)

  # Append all of top string together, new line, all of bottom string, new line, and all the dashes
  appended_string = top_string + "\n" + bottom_string + "\n" + dash_string

  # If answer is required, will add the answer at the very bottom
  appended_string_answer = appended_string + "\n" + answer_string

  print(appended_string_answer)
  
  if display == True:
    return appended_string_answer
  else:
    return appended_string