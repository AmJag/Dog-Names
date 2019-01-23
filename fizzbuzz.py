def greet(title, fname, lname):
  return "Hello, {} {} {}".format(title, fname, lname)

greeting = greet("Mr", "Ewan", "Valentine")

print(greeting)

def dob( day, month, year):
  return "your date of birth is {}/{}/{}".format(day, month, year)

birthday = dob('27','10','1992')

print(birthday)