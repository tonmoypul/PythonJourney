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