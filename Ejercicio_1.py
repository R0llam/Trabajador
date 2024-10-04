from Funcion_1 import*
Nombre_del_libro=str(input("Ingrese el nombre del libro: "))
Tipo_de_libro=str(input("Ingrese el tipo del libro (I)Investigación, (N)Normal: "))
Cantidad_de_paginas=int(input("Ingrese la cantidad de paginas: "))
Costo_del_libro=float(input("Ingrese el costo del libro: "))
Pb=Precio_basico(Costo_del_libro,Cantidad_de_paginas)
Pv=Precio_de_venta(Pb,Cantidad_de_paginas)
if(Tipo_de_libro=="I" or Tipo_de_libro=="i"):
	Extra=Pv*0.02
	Precio_de_venta_Total=Pv+Extra
	Tp="de Investigación"
elif(Tipo_de_libro=="N" or Tipo_de_libro=="n"):
	Precio_de_venta_Total=Pv
	Tp="Normal"
else:
	print("Tipo de libro invalido")
Porcentaje=(Precio_de_venta_Total/Costo_del_libro)*100
print("El nombre del libro es: ",Nombre_del_libro)
print("El tipo es: ",Tp)
print("El precio basico es: ",Pb)
print("El precio de venta es: ",Precio_de_venta_Total)
print("El porcentaje con respecto al costo es: ",Porcentaje,"%")