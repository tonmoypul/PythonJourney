#Input: Principle, Rate, and Time
#
#Output: Interest
#
#Formula:-
#Interest = Principle * (Rate/100) * Time
#
#Principle in TK should be float
#Rate should be calculated via percentage 
#Time must be in year

while True:
  principle = float(input("Enter the principle amount:"))
  if principle < 0.0:
    print("Negative numbers are not allowed. Please input a valid number")
    continue
  elif principle == 0.0:
    print("There is no interest available.")
    continue
  
  rate = float(input("Enter the rate of interest:"))
  if rate < 0.0:
    print("Rate of interest cannot be negative")
    continue
  elif rate == 0.0:
    print("No rate = No interes. Put a rate of interest you want to calculate.")
    continue
  
  timeYear = float(input("Enter time period(year):"))
  timeMonth = float(input("Enter time period(month; if applicable)"))
  if timeYear < 0:
    print("Time cannot be negative")
    continue
  if timeMonth < 0:
    print("Time cannot be negative")
    continue
  elif timeMonth > 12:
    print("Time month should be between 0 to 12")
    continue
  
  time = timeYear + timeMonth/12.0
  interest = principle * rate/100.0 * time
  print(f"You interest is: {interest:.2f}")
  
  choice = input("Do you want to continue? (Y/N)").lower()
  if choice == "y":
    continue
  elif choice == "n":
    break
  else:
    print("Enter valid information yes(y) or no(n)")