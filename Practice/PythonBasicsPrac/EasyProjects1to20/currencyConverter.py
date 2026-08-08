#TK → Dollar
#BDT to USD
#
#
while True:
  bdt = input("Enter BDT amount:")
  if bdt == "stop":
    break
  usd = float(bdt) / 132.0
  print(f"${usd:.2f}")
