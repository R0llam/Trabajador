def Salario_bruto(Sueldo_por_hora,Numero_de_horas_trabajadas):
	Sb=Sueldo_por_hora*(1.5 *(Numero_de_horas_trabajadas - 40) + 40)
	return Sb
def SSO(Sb):
	SSO=Sb*0.06
	return SSO
def Impuesto(Sb,Factor_de_exoneracion):
	Impuesto=(Sb-580*Factor_de_exoneracion)*20/100
	return Impuesto
def Sueldo_neto(Sb,SSO,Impuesto):
	Sn=Sb-SSO-Impuesto
	return Sn