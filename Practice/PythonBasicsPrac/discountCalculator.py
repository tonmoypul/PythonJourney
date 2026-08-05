#Different discount on purchase amount
#
#
while True:
  purchaseAmount = float(input("Enter the purchase amount:"))
  discount = 0.0
  
  if purchaseAmount < 1000:
    discount = 0.05
  elif purchaseAmount < 2000:
    discount = 0.1
  elif purchaseAmount < 5000:
    discount = 0.2
  elif purchaseAmount < 10000:
    discount = 0.4
  else:
    discount = 0.6
  
  discountAmount = float(purchaseAmount * discount)
  finalBill = purchaseAmount - discountAmount
  print(f"Purchase Amount: {purchaseAmount:.2f}\nDiscount Amount: {discountAmount:.2f}\nFinal Price: {finalBill:.2f}")
  
  option = input("Do another item? (Y/N)").lower()
  if option == "y":
    continue
  elif option == "n":
    break
  else:
    print("Invalid")