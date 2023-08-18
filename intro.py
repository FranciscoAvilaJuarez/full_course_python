
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
name = str(input("Please, enter your Name:"))
Lastname = str(input("Please, enter your Lastname:"))
age = int(input("Please, enter your Age:"))
status = str(input("Are You a New Patient? (y)(n)"))

if status.upper() == "N":
    print("Hello")
    print("Welcome", name.capitalize(), Lastname.capitalize(), age, "New Patient")
    print("Hospital X, Welcomes you")

if status.upper() == "Y":
    print("Hello")
    print("Welcome", name.capitalize(), Lastname.capitalize(), age, "Hospital X, Welcomes you")