#Get input from user: rock paper or scissors 
#Give a random output from computer 
#Use the built in random function
#This one is new
#
import random
choices = ["rock", "paper", "scissors"]
while True:
  while True:
    usr = input("Enter your turn (rock, paper, or scissors):").lower()
    
    if usr not in choices:
      print("Input not recognized. Please enter valid input.")
    else:
      break

  com = random.choice(choices)
  result = ""
  
  if (usr == "rock" and com == "scissors") or (usr == "paper" and com == "rock") or (usr == "scissors" and com == "paper"):
    result = "You win! 🎉"
  elif usr == com:
    result = "It is a draw."
  else:
    result = "Computer wins!"
  
  print(f"User input: {usr.title()}\nComputer input: {com.title()}\nResult: {result}")

  while True:
    options = input("Continue? (Y/N)").lower()
    if options == "y":
      break
    elif options == "n":
      break
    else:
      print("Inavlid option.")
  
  if options == "n":
    break