#Input height and weight. Display BMI and category
#Hint: BMI = weight/(height**2)
#Categories: 
#Underweight: BMI less than 18.5
#Healthy Weight: BMI 18.5 to 24.9
#Overweight: BMI 25 to 29.9
#Obesity (Class 1): BMI 30 to 34.9
#Obesity (Class 2): BMI 35 to 39.9
#Severe Obesity (Class 3): BMI 40 or greater
#
#
while True:
  heightInputFoot = float(input("What is your height? (the foot part)"))
  heightInputInces = float(input("What is your height? (the inches part)"))
  weight = float(input("What is your weight? (in kilogram)"))
  
  if heightInputInces >=12:
    print("Height in inches should be between 0 and 11")
    continue
  
  if heightInputFoot <= 0 or heightInputInces < 0 or weight <= 0:
    print("Height and Weight must be a positive number.")
    continue
  
  height = heightInputFoot + heightInputInces/12
  heightInMeter = float(height) * 0.305
  BMI = float(weight) / (heightInMeter**2)

  category = ""
  advice = ""
  
  if BMI < 18.5:
    category = "Underweight"
    advice ="You are underweight. Gain weigh as soon as possible."
  elif BMI <25:
    category = "Healthy Weight"
    advice = "You are healthy. Don't lose your body."
  elif BMI <30:
    category = "Overweight"
    advice ="You are a little bit overweight. Go to gym and gain some muscle instead."
  elif BMI <35:
    category = "Obesity (Class 1)"
    advice = "You have got a lot of weight. Lose weight and be healthy."
  elif BMI <40:
    category = "Obesity (Class 2)"
    advice = "Start going to gym ASAP. Go to the doctor if needed. Overweight is very bad for you."
  else:
    category = "Severe Obesity (Class 3)"
    advice = "Go to the hospital and get medicine also don't forget to maintain diet and gym according to the doctor advice."
  
  print(f"BMI: {BMI:.2f} \nCategory: {category} \n{advice}")
  
  choice = input("Want to continue..?(y/n)").lower()
  if choice == "n":
    break