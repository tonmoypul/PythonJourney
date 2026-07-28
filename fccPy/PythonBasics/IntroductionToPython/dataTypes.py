myIntegerVar = 10
print('Integer:', myIntegerVar, type(myIntegerVar)) #10, <class 'int'>

myFloatVar = 4.60
print('Float:', myFloatVar, type(myFloatVar)) # 4.60, <class 'float'>

myStringVar = 'Hello World!'
print('String:', myStringVar, type(myStringVar)) #Hello World!, <class 'str'>

myBoolVar = True
print('Boolean:', myBoolVar, type(myBoolVar)) #True, <class 'bool'>

mySetVar = {8, 'apple', 7.5}
print('Set:', mySetVar, type(mySetVar)) #{8, 'apple', 7.5}, <class 'set'>

myDictionaryVar = {'name': 'Alice', 'age': 21}
print('Dictionary:', myDictionaryVar, type(myDictionaryVar)) #{'name': 'Alice', 'age': 21}, <class 'dict'>

myTupleVar = (7, 'apple', 8.7)
print('Tuple:', myTupleVar, type(myTupleVar)) #(7, 'apple', 8.7), <class 'tuple'>

myRangeVar = range(10)
print('Range:', myRangeVar, type(myRangeVar)) #range(0,10), <class 'range'>

myList = [22, 'hello', 7.8, True]
print('List:', myList, type(myList)) #[22, 'hello', 7.8, True], <class 'list'>

myNoneVar = None
print('None:', myNoneVar, type(myNoneVar)) #None: None, <class 'NoneType'

print(isinstance(myNoneVar, int))
print(isinstance('hey', int))
print(isinstance(myStringVar, str))
print(isinstance(myIntegerVar, int))


help = 999
print(help, type(help), isinstance(help, int))
print(help, ':call here')



print('Recap of everything')
myInt = 23
print('Int: ' , myInt, type(myInt))
myFloat = 11.8
print('Float: ', myFloat, type(myFloat))
myStr = 'recap'
print('Str: ', myStr, type(myStr))
myBool = False
print('Bool: ', myBool, type(myBool))
mySet = {8, 8.8, 'failed'}
print('Set: ', mySet, type(mySet))
myDict = {'name': 'Failed', 'quality': '∅'}
print('Dict: ', myDict, type(myDict))
myTuple = ('Tonmoy', 0, 100.0)
print('Tuple: ', myTuple, type(myTuple))
myRange = range(78)
print('Range: ', myRange, type(myRange))
myList = [3.54, 3.53, '?']
print('List: ', myList, type(myList))
myNone = None
print('None type: ', myNone, type(myNone))