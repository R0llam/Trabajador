class Rectangulo():
    def __init__ (self,Base,Altura):
        self.Base=Base
        self.Altura=Altura
    def Area(self):
        A=self.Base*self.Altura
        return A
    def Perimetro(self):
        P=(2*self.Base)+(2*self.Altura)
        return P
