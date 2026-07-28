#input(), which lets you prompt the user for input:
name = input("What is your name?")
print(f"Hello, {name}")


def calculate_sum(a, b):
  print(a+b)
#You can see that our function, calculate_sum, has a and b in its parentheses, separated by a comma. Those are called parameters. Think of parameters as placeholder variables that act as "slots" for the values you pass into functions when you call them.

#To use the parameters, you have to pass in "arguments". Arguments are the values you pass to a function when you call it.

#Here's how to call the calculate_sum function to sum together the numbers 3 and 1:

calculate_sum(3, 1) # 4



#Functions also use a special return keyword to exit the function and return a value. If you don't explicitly use return, Python will return None by default.

#Here's an example:
#def calculate_sum(a,b):
#  print(a+b)

#mySum = calculate_subtraction(9,4) #5
#print(mySum) #None

#You can see that the calculate_sum function prints the sum of a and b, but it doesn't return anything explicitly. So when we assign its result to my_sum, the value is actually None. To fix that, you can use the return keyword to send back the result:

#def calculate_sum(a,b):
#   return a+b
#my_sum=calculate_sum(5,4)
#print(my_sum) #9
