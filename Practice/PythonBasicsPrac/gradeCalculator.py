#90+→ A
#80-89 → B
#70-79 → C
#60-69 → D
#0-59 → F
#
#

while True:
  subject = input("Enter subject name:")
  score = float(input("Enter the obtained number:"))
  grade = ""
  
  if score < 60.0:
    grade = "F"
  elif score < 70:
    grade = "D"
  elif score < 80:
    grade = "C"
  elif score < 90:
    grade ="B"
  else:
    grade = "A"
  
  print(f"Subject: {subject} \nObtained grade: {grade}")
  continue 