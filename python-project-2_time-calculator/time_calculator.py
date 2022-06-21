def add_time(start, duration, *start_day):

  print(" ")

  date_dictionary = { 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

  value_dictionary = {day_of_week: value for value, day_of_week in date_dictionary.items()}

  start_split = start.split(":")
  start_minute_split = start_split[1].split(" ")
  start_split = start.split(":")
  
  duration_split = duration.split(":", )

  total_hours = int(start_split[0])+int(duration_split[0])
  total_minutes = int(start_minute_split[0])+int(duration_split[1])
  AM_PM = start_minute_split[1]
  
  if AM_PM == "PM":
    total_hours = total_hours + 12

  days = 0;

  while total_minutes > 60:
    total_minutes = total_minutes - 60
    total_hours = total_hours + 1
    if total_minutes <= 60:
      break    

  while total_hours > 24:
    total_hours = total_hours - 24
    days = days + 1
    if total_hours < 24:
      break

  if total_hours == 24:
    print("24 hr")
    if AM_PM == "PM":
      AM_PM = "AM"
    if AM_PM == "PM":
      AM_PM = "PM"
    days = days + 1
    total_hours = total_hours - 12
  elif total_hours > 12 and total_hours <= 24:
    print("Between 12 and 24 hours")
    AM_PM = "PM"
    total_hours = total_hours - 12
  elif total_hours == 12 and AM_PM == "AM":
    AM_PM = "PM"
  elif total_hours == 12 and AM_PM == "PM":
    AM_PM = "AM"
  elif total_hours < 12:
    AM_PM = "AM"

  # Adds 0 in front of minutes
  if total_minutes < 10:
    new_time = str(total_hours)+":0"+str(total_minutes)+" "+AM_PM
  else:
    new_time = str(total_hours)+":"+str(total_minutes)+" "+AM_PM

  end_day = ""
  for day in start_day:
    day = day.lower()
    day_value = date_dictionary[day]
    print("Start Day is:",day, day_value)
    if days == 0:
      end_day = day.title()
    elif days > 0:
      end_day_value = days + day_value
      end_day_value = end_day_value % 7
      if end_day_value == 0:
        end_day = value_dictionary[7]
      else:
        end_day = value_dictionary[end_day_value]
      end_day = end_day.title()

  if days > 1:
    if end_day != "":
      new_time = new_time+", "+end_day+" ("+str(days)+" days later)"
    else:
      new_time = new_time+" ("+str(days)+" days later)"
  elif days == 1:
    if end_day != "":
      new_time = new_time+", "+end_day+" (next day)"
    else:
      new_time = new_time+" (next day)"
  else:
    if end_day != "":
      new_time = new_time+", "+end_day
    else:
      new_time = new_time
  
  print("start_split:",start_split)
  print("duration_split:",duration_split)

  print("Hours:",start_split[0],duration_split[0],
        "=",total_hours,"days:",days)
  
  print("Minutes:",start_minute_split[0],duration_split[1],
        "=",total_minutes)
  print("New Time:",new_time)
  
  return new_time