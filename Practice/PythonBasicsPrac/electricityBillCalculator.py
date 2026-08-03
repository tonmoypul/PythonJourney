#Input: Bill units
#
#Output:
#Give bill amounts as per unit usage
#
#0-100 units → 5tk per unit
#101-200 units → 7tk per unit
#201+ → 10tk per unit
#
#

while True:
  billUnit = float(input("Enter the unit used:"))
  valuePerUnit = 0.0
  
  if billUnit < 0.0:
    print("Unit usage cannot be negative")
    continue
  elif billUnit < 101.0:
    valuePerUnit = 5.0
  elif billUnit < 201.0:
    valuePerUnit = 7.0
  else:
    valuePerUnit = 10.0
  
  bill = billUnit * valuePerUnit
  print(f"Unit used: {billUnit:.2f} unit\nTotal bill: {bill:.2f} taka")
  
  choice = input("Do you want to continue? (Y/N)").lower()
  if choice == "y" or choice == "yes":
    continue
  elif choice == "n" or choice == "no":
    break
  else:
    print("Invalid option")
    continue