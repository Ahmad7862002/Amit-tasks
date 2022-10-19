import calc



while(True):
  user_in = input("Please Enter the needed operation:\n")
  x = float(input("Enter First Number:\n"))
  y = float(input("Enter Second Number:\n"))

  if(user_in == "add"):
      print(calc.add(x,y))
      x = input("Do you wish to continue?\n")
      if x == "yes":
          continue
      elif x == "stop":
          break
  elif(user_in == "div"):
      print(calc.div(x,y))
      x = input("Do you wish to continue?\n")
      if x == "yes":
          continue
      elif x == "stop":
          break
  elif(user_in == "sub"):
      print(calc.sub(x,y))
      x = input("Do you wish to continue?\n")
      if x == "yes":
          continue
      elif x == "stop":
          break
  elif(user_in == "mult"):
      print(calc.mult(x,y))
      x = input("Do you wish to continue?\n")
      if x == "yes":
          continue
      elif x == "stop":
          break
  else:
      print("Please Enter right operation")


