#Different prices for
#child
#student
#adult
#senior
while True:
  name = input("Enter name:")
  
  category = ""
  age = int(input("Enter age:"))
  price = 0
  
  if age < 10:
    category = "Child"
    price = 100
  elif age <18:
    isStudent = input("Are you a student? (Y/N)").lower()
    if isStudent == "y":
      category = "Student"
      price = 250
    else:
      category = "Young"
      price = 300
  elif age < 30:
    category = "Adult"
    price = 450
  else: 
    category = "General customer"
    price = 500
    
  print(f"Name: {name}\nAge: {age}\nCategory: {category}\nTicket price: {price}")
  
  choice = input("Are there more customers? (Y/N)").lower()
  if choice == "y":
    continue
  elif choice == "n":
    break
  else:
    print("Re-enter correct value")