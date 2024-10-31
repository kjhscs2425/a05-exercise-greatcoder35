import math
format = str(input("Celcius or Fahrenheit?"))
def check_fever():
  if format == "Celcius":
    temperature = float(input("What is your temperature"))
    if (temperature>=44):
      print("You are dead")
    elif (temperature>=38):
      print("You have a fever")
    else:
      print("You don't have a fever")
  elif format == "Fahrenheit":
    temperature = float(input("What is your temperature"))
    if (temperature>=111.2):
      print("You are dead")
    elif (temperature>=100.4):
      print("You have a fever")
    else:
      print("You don't have a fever")

check_fever()
