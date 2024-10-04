Total_Percibido = 0
Valork = float (input ('Ingresa el valor del kilo de Naranjas: '))
for v in range (1, 16):
    print ('Cliente' + repr (v))
    KilosC= float (input ('Ingrese los kilos comprados: '))
    Total=KilosC*Valork
    if KilosC>=10:
        Descuento=Total*0.15
    else:
        Descuento=0
    Totalap=Total-Descuento
    Total_Percibido=Total_Percibido+Totalap
    print ('Valor del descuento: ' + repr (Descuento))
    print ('Valor total: ' + repr (Total))
    print ('Valor total a pagar: ' + repr (Totalap))
print ('total percibido por la tienda: ' + repr (Total_Percibido))
