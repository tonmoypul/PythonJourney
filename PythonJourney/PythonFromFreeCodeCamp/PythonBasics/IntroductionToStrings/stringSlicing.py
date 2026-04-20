#Basic syntax
#myStr = 'ajakajakskaksak'
#print(myStr[start:stop:step(optional)])

#Some examples
newStr = 'hello world'
print(newStr[2:5])
print(newStr[2:])
print(newStr[:4])
print(newStr[:])
print(newStr[2:6:3])

#Reversing a string using slice method
myStr = 'Hello World'
reverseOfMyStr = myStr[::-1]
print(reverseOfMyStr)