def Sueldo_nuevo(Sueldo,AS,Numeros_de_cursos):
	if(AS>=5):
		SN=Sueldo + (Sueldo*0.10)
	else:
		SN=Sueldo
	if(Numeros_de_cursos>=4):
		Sueldo_nuevo=SN+250
	else:
		Sueldo_nuevo=SN
	return Sueldo_nuevo