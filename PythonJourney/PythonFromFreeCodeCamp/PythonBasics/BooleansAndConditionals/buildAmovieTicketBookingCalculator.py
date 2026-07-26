basePrice = 15
age = 21
seatType = "Gold"
showTime = "Evening"
if age>17:
  print("User is eligible to buy a ticket")
  
if age>=21:
  print("User is eligible for Evening shows")
else:
  print("User is not eligible for Evening shows")

isMember = True
isWeekend = False
discount = 0

if isMember:
  discount = 3
  print("User qualifies for membership discount")
else:
  print("User does not qualify for membership dicount")
print,("Discount:", discount)

