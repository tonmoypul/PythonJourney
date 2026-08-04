#Correct username and password are stored in variables
#
#

username = "Tonmoy Pul"
password = "240101020"

while True:

  usrnameInput = input("Enter your username:")

  if username == usrnameInput:
    pswordInput = input("Enter your password:")
    if password == pswordInput:
      print("Welcome to the website")
      break
    else:
      print("Incorrect password")
  else:
    print("Inavlid username")
  