isFriend = True
smoker = True

if isFriend:
    if not smoker:
      print("He is cricket partner")
    else:
      print("He is buddy")
else:
    print("He is normal close friend.")

isCitizen = False
age = 19

if isCitizen and age >=18:
  print("You are eligible to vote")
else:
  print("You are not eligible to vote")
  
  
isStudent = False
age = 17

if isStudent or age <=18:
  print("You can get a discount")
else:
  print("Sorry but you are not eligible to get the student discount")
  
hasGF = False

if not hasGF:
  print("You're lucky")
else:
  print("Shame on you")