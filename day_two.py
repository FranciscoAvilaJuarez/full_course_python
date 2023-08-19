
## ask user their weight and convertl it and print it on terminal
convert = float(0.450)

print("hello, there! ")
peso = int(input("what is your weight? "))
tipo = str(input("is this in (K)g or (L)bs?"))
if tipo == "k":
    new_Pound = peso * convert
    print("this is your Weight in Pounds:", int(new_Pound))

elif tipo == "l":
    new_peso = peso/convert
    print("This is your Weight in Kilos:", int(new_peso))
