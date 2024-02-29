nom=str(input("ingrese el nombre del trabajador: "))
montoV=float(input("ingrese el monto de venta: "))
AS=float(input("ingrese los años de servicio: "))
if(montoV<5000):
	comision=montoV * 0.05
elif(montoV>=5000 and montoV<10000):
	comision=montoV * 0.07
elif(montoV>=10000 and montoV<100000):
	comision=montoV * 0.08
else:
	comision=montoV * 0.10
if(AS>7 and AS<=15):
	comisiont=comision * 2
elif(AS>15):
	extra=(AS - 15) * 500
	comisiont=comision * 2 + extra
else:
	comisiont=0
print("la comision del empleado",nom,"es: ",comisiont)
