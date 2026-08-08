#Add VAT with each restaurant bill
#
#

while True:
  name = input("Enter customer name:")
  bill = float(input("Enter the bill:"))
  
  while True:
    tax = float(input("Enter tax percentage:"))
    if tax <= 0:
      print("Tax must be greater than 0")
    else:
      break
  
  taxAmount = bill * tax / 100
  totalBill = taxAmount + bill
  
  print(f"Primary bill: {bill:.2f}\nTax amount: {taxAmount:.2f}\nFinal bill(VAT included): {totalBill:.2f}")
  
  while True:
    billStatus = input("Is bill paid?(Y/N)").lower()
    if billStatus == "y":
      print(f"Thanks for coming to us {name}")
      break
    elif billStatus == "n":
      paymentMethod = input("Cash or Card sir?").lower()
      if paymentMethod == "card":
        while True:
          pin = input("Here you go sir, give your pin here:")
          if pin == "1234":
            print("Thanks for coming sir")
            break
          else:
            print("Please make the payment sir...")
            continue
        break
      else:
        print("Thank you sir. You are always welcome to come.")
        break
    else:
      print("Enter valid value")
      continue

  choice = input("Wanna comtinue?(Y/N)").upper()
  if choice == "Y":
    continue
  elif choice == "N":
    break
  else:
    print("I didn't learn to deal with this, yet...")