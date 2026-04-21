#How to get a string to all uppercase or lowercase?
myStr = 'Hello World!'
upperCaseStr = myStr.upper()
print(upperCaseStr)
lowercaseStr = myStr.lower()
print(lowercaseStr)

#Strip method
stripedStr = myStr.strip('Hd!')
print(stripedStr)

stripedStr1 = myStr.strip("")
print(stripedStr1)

stripedStr2 = myStr.lstrip('He')
print(stripedStr2)

stripedStr3 = myStr.rstrip('ld!')
print(stripedStr3)

#Replace method
newStr = 'The old bull hit the old truck and broke it in parts. The owner was very angry at the bull and sold it to the neighbour.'
print(newStr.replace('the', 'his'))

newStr = newStr.replace('the', 'his')

#Split method
splitedStr = newStr.split()
print(splitedStr)
print(newStr.split('.'))

#Join method on iterables
joinedList = '###'.join(splitedStr)
print(joinedList)

#startswith(prefix) & endswith(suffix) method
newStr = 'The old bull hit the old truck and broke it in parts. The owner was very angry at the bull and sold it to the neighbour.'

startsWithPrefix = newStr.startswith('The')
print(startsWithPrefix) #True
endsWithSuffix = newStr.endswith('neighbour')
print(endsWithSuffix) #False

#finding index of a substring and number of times a substring jas appeared on a string
print(newStr.find('hit'))
print(newStr.count('the'))

#capitalize method
newNewStr = 'hello world'
print(newNewStr.capitalize())

#checking if all words are on uppercase or lowercase in a string
print(newNewStr.isupper())
print(newNewStr.islower())

#title method
print(newNewStr.title())