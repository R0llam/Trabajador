Tamano=int(input("Ingrese el tamaño de la pizza 1, 2 o 3: "))
Cantidad_Ingredientes=int(input("Ingrese la Cantidad de ingredientes extra: "))
if(Tamano==1):
    Monto_Cancelar=25+(Cantidad_Ingredientes*4)
elif(Tamano==2):
    Monto_Cancelar=30+(Cantidad_Ingredientes*4)
elif(Tamano==3):
    Monto_Cancelar=40+(Cantidad_Ingredientes*4)
else:
    Monto_Cancelar=0
print("el monto a cancelar es: ", Monto_Cancelar)
