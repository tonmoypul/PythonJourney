anikTotalMeal = 42
tonuTotalMeal = 45
chondonTotalMeal = 48
prantoTotalMeal = 54
jeetTotalMeal = 65
siddharthoTotalMeal = 46
tonmoyTotalMeal = 63

anikJoma = 3000
tonuJoman = 3000
chondonJoma = 1500
prantoJoma = 2500
jeetJoma = 1000
siddharthoJoma = 1000
tonmoyJoma = 2000

totalMeal = anikTotalMeal + tonuTotalMeal + chondonTotalMeal + prantoTotalMeal + jeetTotalMeal + siddharthoTotalMeal + tonmoyTotalMeal

dokanDue = 7000
totalBazarKhoroch = 0 #Somehow you have to make this work as the sum of all the amounts of bazar of the whole month. Do not just add up it for yourself but just somehow make it like this that you can daly add the expenses whenever you come from bazar
totalExpenses = totalBazarKhoroch + dokanDue

def mealRate():
  return totalExpenses/totalMeal

