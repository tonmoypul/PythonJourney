#Input: A number
#Output: Whether the given number is odd or even

while True:
  num = int(input("Enter the number:"))
  
  if num % 2 == 0:
    print("The number is even")
  else:
    print("The number is odd")
  
  choice = input("Want to verify another number? (Y/N)").lower()
  if choice == "y":
    continue
  elif choice == "n":
    break
  else:
    print("Enter a valid value")