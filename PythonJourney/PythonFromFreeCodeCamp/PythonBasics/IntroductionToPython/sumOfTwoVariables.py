num1 = 23
num2 = 65
#Sum of two numbers
def sum(num1,num2) :
  return num1 + num2
print(sum(num1, num2))
print(sum(78, 89))
print(sum('asd', 'ggg'), type(sum))

#Remainder of any two numbers 
def remainderOfTwoNumbers(dividend, dividor) : 
  remainder = dividend % dividor
  return remainder
print(remainderOfTwoNumbers(45728292,8))

#Sum of any arithmetic series 
def sumOfSeries(startingNumber, endingNumber) :
  i = startingNumber
  sum = 0
  while i<=endingNumber:
    sum = sum + i
    i = i + 1
  return sum
    
print(sumOfSeries(1,19))

#Checking if a number is odd or even
print('Checking if a number is odd or even')
number = 6783795
if number%2==0:
  print('The number is even')
else:
  print('The number is odd')
  
#Sum of a series of odd numbers
def sumOfOddNumbers(startingNumber1, endingNumber1) :
  j = startingNumber1
  total = 0
  if j%2==0:
    j = j + 1
    while j<=endingNumber1:
      total = total + j
      j = j +2
  else:
    while j<=endingNumber1:
      total = total + j
      j = j+ 2
  return total

print(sumOfOddNumbers(34, 67))

#Sum of a series of even numbers
print('Sum of a series of even numbers')
def sumOfEvenNumbers(startingNumber2, endingNumber2):
  evenSum = 0
  l = startingNumber2
  if l%2!=0:
    l=l+1
  while l<=endingNumber2:
    evenSum = evenSum + l
    l=l+2
  return evenSum
print(sumOfEvenNumbers(89,99))

#Finding a prime number
def primeNumber(theGivenNum):
  if theGivenNum<=1:
    return 'The number is not prime'
  rootOfTheNunber = theGivenNum**0.5
  for divisors in range(2, int(rootOfTheNunber)+1):
    if theGivenNum%divisors == 0:
      return 'The number is not prime'
  return 'The number is prime'
print(primeNumber(73))

#Fibonacci sequence 
#def fibonacciSequenceSum(theNumberOfFibonacciCharectersToSum)