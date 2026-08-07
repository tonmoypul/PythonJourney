#Area of different shapes:
#Rectangle: 
#Given length=x and width=y
#area = x*y
#
#Circle:
#Given radius r
#area = pi * (r ** 2); where pi = 3.14159
#
#Triangle:
#Given base = b and height = h
#area = (1/2) * b * h
#
#Given 2 connected sides a and b, and the angle between them
#area = (1/2) * a * b * math.sin(angle)
#
#Given three sides a, b, c
#area = (s * (s-a) * (s-b) * (s-c)) ** (1/2)
#
#Given it is a equilateral triangle (somobahu)
#area = ((3**(1/2))/4) * a**2
#
#Given it is a isotherm (somo dibahu)
#soman soman bahu = a, base = b
#area = (b * (4*(a**2) - b**2) ** (1/2))/4

import math
while True:
  shape = input("Enter the shape (Rectangle, Circle, Triangle):").title()
  while True:
    unit = input("What is the unit of side?(m or cm or inch)").lower()
    factor = 0
    if unit == "m":
      factor = 1
      break
    elif unit == "cm":
      factor = 0.01
      unit = "m"
      break
    elif unit == "inch":
      factor = 0.0254
      unit = "m"
      break
    else:
      print("Unit not recognized")
      continue
  length = 0
  width = 0
  height = 0
  a = 0
  b = 0
  c = 0
  area = 0
  radius = 0
  base = 0
  theta = 0
  s = 0
  
  if shape == "Rectangle":
    length = float(input("Enter the length:")) * factor
    width = float(input("Enter the width:")) * factor
    area = length * width
  elif shape == "Circle":
    radius = float(input("Enter the value of radius:")) * factor
    area = 3.14159 * radius**2
  elif shape == "Triangle":
    while True:
      type = input("What kind of triangle is it? (general, 2 sides and angle, 3 sides, equilateral, isotherm)").lower()
      if type == "general":
        base = float(input("Enter the base of the triangle:")) * factor
        height = float(input("Enter the height of the triangle:")) * factor
        area = (base * height) / 2
        break
      elif type == "2 sides and angle":
        a = float(input("Enter value of one side:")) * factor
        b = float(input("Enter value of other side:")) * factor
        theta = float(input("Enter the angle (in degrees):"))
        area = (a * b * math.sin(math.radians(theta)))/2
        break
      elif type == "3 sides":
        a = float(input("Enter value of first side:")) * factor
        b = float(input("Enter value of second side:")) * factor
        c = float(input("Enter value of third side:")) * factor
        s = (a + b + c)/2
        area = (s * (s-a) * (s-b) * (s-c)) ** (1/2)
        break
      elif type == "equilateral":
        a = float(input("Enter value of the sides:")) * factor
        area = (3/16)**(1/2) * a**2
        break
      elif type == "isotherm":
        a = float(input("Enter value of the same same side:")) * factor
        b = float(input("Enter value of the base:")) * factor
        area = (b * (4*(a**2) - b**2) ** (1/2))/4
        break
      else:
        print("Invalid option")
        continue
  else:
    print("Shape not recognized")
    continue
  
  print(f"The area of your {shape} is {area} {unit}²")
  
  choice = input("Want more? (Y/N)").lower()
  if choice == "y":
    continue
  elif choice == "n":
    break
  else:
    print("Invalid option")
    continue