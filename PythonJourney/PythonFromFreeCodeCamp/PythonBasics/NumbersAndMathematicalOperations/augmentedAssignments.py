#The basic syntax of augmented assignment looks like this
# variable <operation>= value
# Which is more efficient way of doing this
# variable = variable <operation> value

myVar = 10
#Addition using augmenetd assignment 
myVar += 5
print(myVar)
#Subtraction using augmenetd assignment 
myVar -= 7
print(myVar)
#Multiplication using augmenetd assignment 
myVar *=4
print(myVar)
#Division using augmenetd assignment 
myVar /= 4
print(myVar)
#Floor using augmenetd assignment 
myVar //= 3
print(myVar)
#Modulo using augmenetd assignment 
myVar %= 6
print(myVar)
#Exponentiation using augmented assignment
myVar **=6
print(myVar)

#Addition of two strings
myStr = "Hello"
myStr += "World"
print(myStr)
#Exponentiation of strings
myStr *=2
print(myStr)