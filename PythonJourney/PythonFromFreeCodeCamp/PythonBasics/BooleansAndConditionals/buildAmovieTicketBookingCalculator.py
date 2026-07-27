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

extraCharges = 0
if isWeekend or showTime == "Evening":
  extraCharges = 2
  print("Extra charges will be applied")
else:
  print("No extra charges will be applied")
print("Extra charges:", extraCharges)

if age >=21 or age>=18 and (showTime != "Evening" or isMember):
  print("Ticket booking condition satisfied")
  
  serviceCharges = 0
  if seatType == "Premium":
    serviceCharges = 5
  elif seatType == "Gold":
    serviceCharges = 3
  else:
    serviceCharges = 1
  print("Service charges:", serviceCharges)
  finalPrice = basePrice + extraCharges + serviceCharges - discount
  print("Final price of ticket:", finalPrice)
else:
  print("Ticket booking condition not satisfied")