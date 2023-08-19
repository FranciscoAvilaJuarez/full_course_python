# Import date class from datetime module
from datetime import date

print("francisco avila")
print("o_____o")
print(" ||||")
print("*"*10)

price = 10
print(price)
price = 20
print(price)


#   name: john smith, age: 20 yrs old, patient: new
print("Welcome to Hospital X")

Name = str(input("Please, enter your Name: "))
Lastname = str(input("Please, enter your Lastname: "))
Age = int(input("Enter the Year you were Born: "))
status = str(input("Are You an (A)ctive or a (N)ew Patient? "))


# Returns the current local date
today = date.today()
print(today)
Edad = today.year - int(Age)    #nice, my idea

if status.upper() == "N":
    Social = int(input("Please, Enter your Social: "))
    print("Hello,")
    print("Welcome,", Name.capitalize(), Lastname.capitalize())
    print("New Patient,", "Age:", Edad, "with Social:", Social)
    print("Hospital X, Welcomes You")

elif status.upper() == "A":
    print("Hello,")
    print("Welcome,", Name.capitalize(), Lastname.capitalize(), "Age:", Edad)
    print("Hospital X is Happy to See You!")


year_born: int = int(input("enter the year you were born "))
age = today.year - year_born
print(Name, "your age is:", age)
