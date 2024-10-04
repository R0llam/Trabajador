class Vehiculo():
    def __init__(self,Color,Marca,Modelo,Numero_de_puertas,Numero_de_matricula):
        self.Color=Color
        self.Marca=Marca
        self.Modelo=Modelo
        self.Numero_de_puertas=Numero_de_puertas
        self.Numero_de_matricula=Numero_de_matricula
    def Mostrar_Color(self):
        print("El color del vehículo es: ",self.Color)
    def Mostrar_Marca(self):
        print("La marca del vehículo es: ",self.Marca)
    def Mostrar_Modelo(self):
        print("El modelo del vehículo es: ",self.Modelo)
    def Mostrar_Numero_de_puertas(self):
        print("El numero de puertas del vehículo es: ",self.Numero_de_puertas)
    def Mostrar_Numero_de_matricula(self):
        print("El numero de matricula del vehículo es: ",self.Numero_de_matricula)
