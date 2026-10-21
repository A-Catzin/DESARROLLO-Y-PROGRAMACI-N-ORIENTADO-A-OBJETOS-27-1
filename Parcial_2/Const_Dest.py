class Archivo:
    def __init__(self,nombre):
        self.nombre = nombre
        print("Objeto creado")

    def __del__ (self,):
        print("Objeto eliminado")

HojaTXT = Archivo("datos.txt")
print(HojaTXT.nombre)
del HojaTXT
