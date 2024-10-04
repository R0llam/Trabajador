def Pago_por_horas_extra(Numero_de_horas_trabajadas,Valor_de_la_hora):
	if(Numero_de_horas_trabajadas>48):
		PPHE=(Numero_de_horas_trabajadas - 48)*(Valor_de_la_hora*0.35)
	else:
		PPHE=0
	return PPHE
def Pago_neto(PPHE,Numero_de_horas_trabajadas,Valor_de_la_hora,Sueldo_base):
	P_n=(Numero_de_horas_trabajadas*Valor_de_la_hora)+Sueldo_base+PPHE
	return P_n