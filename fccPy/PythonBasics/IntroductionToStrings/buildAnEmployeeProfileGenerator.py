first_name = 'John'
last_name = 'Doe'
fullName = first_name + ' ' + last_name
employeeAge = 28
employeeInfo = f'{fullName} is {employeeAge} years old'
print(employeeInfo)
experienceYears = 6
experienceInfo = f'Experience: {experienceYears} years'
print(experienceInfo)
posiiton = 'Cyber Expert'
salary = 80000
employeeCard = f'Employee: {fullName} | Age: {employeeAge} | Position: {posiiton} | Salary: ${salary}'
print(employeeCard)

employeeCode = 'CYBER-2026-CS-001'
department = employeeCode[0:5]
print(department)
yearCode = employeeCode[6:10]
print(yearCode)
initials = employeeCode[-6:-4]
print(initials)
lastThree = employeeCode[-3:]
print(lastThree)