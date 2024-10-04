def N(N1,N2,N3):
    if(N1>N2 and N1>N3):
        print("El valor maximo es:",N1)
    elif(N1>N2 and N1==N3):
        print("El valor maximo es el segundo y tercer valor ",N1)
    elif(N1==N2 and N1>N3):
        print("El valor maximo es el primer numero y el segundo valor:",N1)
    elif(N2>N1 and N2>N3):
        print("El valor maximo es:",N2)
    elif(N2>N1 and N2==N3):
        print("El valor maximo es el segundo numero y el Tercer valor",N2)
    elif(N3>N1 and N3>N2):
        print("El valor maximo es:",N3)
    else:
        print("Los tres valores son iguales")
