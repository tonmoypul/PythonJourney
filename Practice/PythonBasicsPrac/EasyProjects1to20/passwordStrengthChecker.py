#Rules:
#length >=8
#contains digit
#contains uppercase
#contains lowercase
#
#

password = "233738392993abcdAbCD4020"
alphabet = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"

if len(password) >= 8:
  if any(char in password for char in alphabet.lower()) and any(chr in password for chr in alphabet.upper()):
    if any(c in password for c in digit):
      print("It is a very strong password")
    else:
      print("Your password is strong but add some digits to make it better")
  else:
    print("Reset your password with a strong one.")
else:
  print("This is not a kind of password. Fix it by adding uppercase, lowercase alphabets and digits")