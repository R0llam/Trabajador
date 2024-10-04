R=0
TG=str(input("Ingrese el tipo de gasolina A, B o C. Ingrese D para finalizar: "))
while(TG!="D" and TG!="d"):
    G=float(input("Ingrese la cantidad de galones vendidos: "))
    if(TG=="A" or TG=="a"):
        PresioG=50 * 3.785
        PaP=PresioG * G
    elif(TG=="B" or TG=="b"):
        PrecioG=55 * 3.785
        PaP=PrecioG * G
    elif(TG=="C" or TG=="c"):
        PrecioG=60 * 3.785
        PaP=PrecioG * G
    else:
        print("error tipo de gasolina invalido")
        PaP=0
    R=R + PaP
    print("el cliente debe pagar",PaP)
    TG=str(input("Ingrese el tipo de gasolina A, B o C. Ingrese D para finalizar: "))
print("el total recaudado por la gasolineria es: ",R)
