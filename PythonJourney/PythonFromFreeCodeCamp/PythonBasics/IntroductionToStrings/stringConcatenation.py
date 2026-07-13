#Concatenating two strings
firstString = "Hello"
secondString = "World!"
concatenatedString = firstString + ' ' + secondString
print(concatenatedString)

#Concatenating a string with integer or other objects
stringVar = 'John'
integerVar = 25

string_Integer_Var = stringVar + ' ' + str(integerVar)
print(string_Integer_Var)

#Augmented assignment operator "+=" for concatenation
name = 'John Doe'
age = 26

name_and_age = name
name_and_age += str(age)
print(name_and_age)

#String Interpolation
#The process of inserting variables and expressions into a string is called string interpolation. Python has a category of string called f-strings (short for formatted string literals), which allows you to handle interpolation with a compact and readable syntax.
#F-strings start with f (either lowercase or uppercase) before the quotes, and allow you to embed variables or expressions inside replacement fields indicated by curly braces ({}). 
nameAgeInterpolation = f'My name is {name}. And I am {age} years old.'
print(nameAgeInterpolation)

num1 = 36
num2 = 56
print(F"The sum of {num1} and {num2} is 92.")

print('Hello World!')

#Augmented assignment operator
name="john doe"
age=24
nameAge=name
nameAge+=str(age)
print(nameAge)