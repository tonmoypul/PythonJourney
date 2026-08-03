#Celcius → Fahrenheit 
#Fahrenheit → Celcius
#
#C = (F-32)* 5/9
#F = 9C+32
#
#Input 1: Value of temperature 
#Input 2: Unit of the temperature
#
#Output: Value + Unit of the converted temperature

while True:
  temperature = float(input("Give the value of temperature here:"))
  unit = input("What is the unit of the temperature? (C/F)").lower()
  
  celciusConvert = (temperature - 32.0) * (5.0/ 9.0)
  fahrenheitConvert = (temperature * (9.0/5.0)) + 32.0
  
  if unit == "c" or unit == "celcius":
    print(f"Given temperature: {temperature:.2f} {unit} \nConverted temperature: {fahrenheitConvert:.2f} °F")
  elif unit == "f" or unit == "fahrenheit":
    print(f"Given temperature: {temperature:.2f} {unit} \nConverted temperature: {celciusConvert:.2f} °C")
  else:
    print("The unit is invalid. Please put a valid unit.")
    continue
  
  choice = input("Do you want to continue? (Y/N)").lower()
  if choice == "y":
    continue
  elif choice == "n":
    break
  else:
    print("Enter a valid option: (Y/N)")