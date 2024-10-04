def Precio_basico(Costo_del_libro,Cantidad_de_paginas):
	Pb=Costo_del_libro+(Cantidad_de_paginas*0.75)
	return Pb
def Precio_de_venta(Pb,Cantidad_de_paginas):
	if(Cantidad_de_paginas>300 and Cantidad_de_paginas<=500):
		Pv=Pb+500
	elif(Cantidad_de_paginas>500):
		Extra=(Cantidad_de_paginas-500)*2
		Pv=Pb+500+Extra
	else:
		Pv=Pb
	return Pv