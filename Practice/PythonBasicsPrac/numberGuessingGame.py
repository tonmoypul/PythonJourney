#Take a number from user
#Match it with a number from random on computer
#If matches then user wins
#If not then try again

import random
number = list(range(1,21))
while True:
  num = random.choice(number)
  while True:
    usr = int(input("Enter a number between 1 to 20:"))
    if usr not in number:
      print("Pleas enter valid number between 1 to 20")
      continue
    else:
      if usr == num:
        print("You have won the game")
        break
      else:
        print("Try again")
    
  while True:
    choice = input("Continue? (Y/N)").lower()
    if choice == "y":
      break
    elif choice == "n":
      break
    else:
      print("Enter valid option")
  if choice == "n":
    break