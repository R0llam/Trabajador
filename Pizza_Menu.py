Salida=False
while not Salida:
    print("1) Pizza pequeña")
    print("2) Pizza mediana")
    print("3) Pizza grande")
    print("4) Salida")
    opcion=input("Elija una opcion: ")
    if opcion=="1":
        Cantidad_de_ingredientes=int(input("Ingrese la cantidad de ingredientes: "))
        Precio_total=(Cantidad_de_ingredientes * 5)+25
        print("La cantidad de ingredientes extra es: ",Cantidad_de_ingredientes)
        print("El valor a pagar es: ",Precio_total)
    elif opcion=="2":
        Cantidad_de_ingredientes=int(input("Ingrese la cantidad de ingredientes: "))
        Precio_total=(Cantidad_de_ingredientes * 5)+40
        print("La cantidad de ingredientes extra es: ",Cantidad_de_ingredientes)
        print("El valor a pagar es: ",Precio_total)
    elif opcion=="3":
        Cantidad_de_ingredientes=int(input("Ingrese la cantidad de ingredientes: "))
        Precio_total=(Cantidad_de_ingredientes * 5)+60
        print("La cantidad de ingredientes extra es: ",Cantidad_de_ingredientes)
        print("El valor a pagar es: ",Precio_total)
    elif opcion=="4":
        Salida=True
    else:
        print("opcion invalida")
