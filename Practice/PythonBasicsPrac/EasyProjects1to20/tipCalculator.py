#Input bill amount and tip percentage
#Output: Tip amount, Total amount
#
#

while True:
  bill = float(input("Your bill is: "))
  tip = float(input("What percent you wanna tip?"))
  
  if bill < 0.0:
    print("Bill amount should be a positive number")
    continue
  elif bill == 0.0:
    print("Are we giving free food today?? 😵‍💫")
  
  if tip <=0:
    print("Don't be so rude 😞")
    continue
  
  tipPercentage = tip/100.0
  tipAmount = bill * tipPercentage
  totalBill = bill + tipAmount

  print(f"Food bill: {bill} \nTip amount: {tipAmount} \nTotal bill: {totalBill}")