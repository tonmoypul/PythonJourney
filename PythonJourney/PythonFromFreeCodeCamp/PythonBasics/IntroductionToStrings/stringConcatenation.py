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
