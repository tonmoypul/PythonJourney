#Check whether three sides can form a triangle
#Hint:
#a+b>c
#b+c>a
#c+a>b
while True:
  sideA = float(input("Enter the value of first side:"))
  if sideA <= 0:
    print("Side can't be negative or zero")
    continue
  
  while True:
    sideB = float(input("Enter the value of second side:"))
    if sideB <= 0:
      print("Side can't be negative or zero")
    else:
      break
  
  while True:
    sideC = float(input("Enter the value of third side:"))
    if sideC <= 0:
      print("Side can't be negative or zero")
    else:
      break
  
  if (sideA + sideB > sideC) and (sideB + sideC > sideA) and (sideC + sideA > sideB):
    print(f"{sideA}, {sideB}, {sideC} form a triangle")
  else:
    print(f"{sideA}, {sideB}, {sideC} cannot form a triangle")
  
  choice = input("Do you want more? (y/n)")
  if choice == "y":
    continue
  elif choice == "n":
    break