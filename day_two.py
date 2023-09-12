
## ask user their weight and convertl it and print it on terminal
convert = float(0.450)

print("Hello, There, Friend! ")
Peso = int(input("What is your Weight? "))
Tipo = str(input("Is this in (K)g or in (L)bs?"))

#convert to pound
if Tipo == "k":
    new_Pound = Peso * convert
    print("this is your Weight in Pounds:", int(new_Pound))

#convert to kilo
elif Tipo == "l":
    new_peso = Peso/convert
    print("This is your Weight in Kilos:", int(new_peso))
