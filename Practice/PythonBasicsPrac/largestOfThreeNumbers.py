#Given three numbers
#Find the largest of these three numbers
#
#

num1 = 23
num2 = 569
num3 = 67

if num1 > num2:
  if num1 > num3:
    print(f"Number 1: {num1} is largest")
  else:
    print(f"Number 3: {num3} is largest")
else:
  if num2 > num3:
    print(f"Number 2: {num2} is largest")
  else:
    print(f"Number 3: {num3} is largest")
    
#
#
#Python has a built-in function to compare and give the largest if three numbers
#
#
print(f"The largest of the numbers is {max(num1, num2, num3)}")