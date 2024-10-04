from Funcion_4 import*
Nombre_del_empleado=str(input("Ingrese el nombre del empleado: "))
Sueldo=float(input("Ingrese el sueldo: "))
AS=float(input("Ingrese los años de servicio: "))
Numeros_de_cursos=int(input("Ingrese el numeros de cursos realizados: "))
Sueldo_nuevo=Sueldo_nuevo(Sueldo,AS,Numeros_de_cursos)
print("El sueldo nuevo del empleado",Nombre_del_empleado,"es: ",Sueldo_nuevo)