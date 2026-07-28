isRainy = input("Is it rainy? (True/False)") == "True"
isMorning = input("Is it morning? (True/False)") == "True"
moneyStatus = int(input("Money in pocket: "))
# The built-in input() returns a string


def canWeTravel():
  if moneyStatus == 0:
    return "Tour cancel"
  elif moneyStatus >=500:
    if not isRainy and isMorning:
      return "Let's go to the tour boys"
    else:
      return "Tour cancel due to weather"
  else:
    return "Not enough money, tour cancel"

print("Decision: ", canWeTravel())