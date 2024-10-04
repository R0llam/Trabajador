class Articulo():
    def __init__(self,cd,cantidad,precio):
        self.condigo=cd
        self.cantidad=cantidad
        self.precio=precio
    def mostrar_cantidad(self):
        print("Cantidad actual: ",self.cantidad)
    def mostrar_precio(self):
        print("Precio ",self.precio)
    def Vender(self,x):
        if(x<=self.cantidad):
            self.cantidad=self.cantidad-x
        else:
            print("Cantidad insuficiente")
    def comprar(self,x):
        self.cantidad=self.cantidad+x
