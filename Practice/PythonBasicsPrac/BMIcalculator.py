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
  heightInputFoot = input("What is your height? (the foot part)")
  heightInputInces = input("What is your height? (the inches part)")
  weight = input("What is your weight? (in kilogram)")
  
  
  if int(heightInputFoot) < 0 or int(heightInputInces) < 0 or int(weight) < 0:
    print("Height and Weight must be a positive number.")
    break
  
  height = float(heightInputFoot) + float(heightInputInces)/12
  heightInMeter = float(height) * 0.305
  BMI = float(weight) / (heightInMeter**2)

  category = ""
  if BMI < 18.5:
    category = "Underweight"
  elif BMI >= 18.5 and BMI <= 24.9:
    category = "Healthy Weight"
  elif BMI >= 25 and BMI <= 29.9:
    category = "Overweight"
  elif BMI >= 30 and BMI <= 34.9:
    category = "Obesity (Class 1)"
  elif BMI >= 35 and BMI <= 39.9:
    category = "Obesity (Class 2)"
  elif BMI >= 40:
    category = "Severe Obesity (Class 3)"

  if BMI < 18.5:
    print(f"BMI: {BMI:.2f} \nCategory: {category} \nYou are underweight. Gain weigh as soon as possible.")
  elif BMI >= 18.5 and BMI <= 24.9:
    print(f"BMI: {BMI:.2f} \nCategory: {category} \nYou are healthy. Don't lose your body.")
  elif BMI >= 25 and BMI <= 29.9:
    print(f"BMI: {BMI:.2f} \nCategory: {category} \nYou are a little bit overweight. Go to gym and gain some muscle instead.")
  elif BMI >=30 and BMI <= 34.9:
    print(f"BMI: {BMI:.2f} \nCategory: {category} \nYou have got a lot of weight. Lose weight and be healthy.")
  elif BMI >=35 and BMI <= 39.9:
    print(f"BMI: {BMI:.2f} \nCategory: {category} \nStart going to gym ASAP. Go to the doctor if needed. Overweight is very bad for you.")
  elif BMI >= 40:
    print(f"BMI: {BMI:2f} \n Category: {category} \n Go to the hospital and get medicine also don't forget to maintain diet and gym according to the doctor advice.")
    
  choice = input("Want to continue..?(y/n)")
  if choice == "n":
    break