Cedula=str(input("Ingrese la Cedula: "))
Nombre=str(input("Ingrese el Nombre: "))
Direccion=str(input("Ingrese la Direccion: "))
Sueldo=float(input("Ingrese el Sueldo: "))
Monto_Ventas=float(input("Ingrese el monto de ventas: "))
if(Monto_Ventas>60000):
    Bono=Monto_Ventas * 0.20
else:
    Bono=Monto_Ventas * 0.10
SueldoTotal=Sueldo + Bono
print("La Cedula del Trabajador es: ",Cedula)
print("El Nombre del Trabajador es: ",Nombre)
print("El Sueldo Total del Trabajador es: ",SueldoTotal)
