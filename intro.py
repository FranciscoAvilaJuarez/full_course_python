
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
Age = int(input("Please, enter your Age: "))
status = str(input("Are You an (A)ctive or a (N)ew Patient? "))

if status.upper() == "N":
    Social = int(input("Please, Enter your Social: "))
    print("Hello,")
    print("Welcome,", Name.capitalize(), Lastname.capitalize())
    print("New Patient,", "Age:", Age, "with Social:", Social)
    print("Hospital X, Welcomes You")

if status.upper() == "A":
    print("Hello,")
    print("Welcome,", Name.capitalize(), Lastname.capitalize(), "Age:", Age)
    print("Hospital X is Happy to See You!")
