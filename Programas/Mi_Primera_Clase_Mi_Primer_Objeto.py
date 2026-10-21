#Mi primera clase mi primer objeto  

class Hoil:
#Función del constructor/inicializador 
    def __init__(self,nombre,especie,edad):
        #Atributos 
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    #Definicion de metodos 
    def presentar (self):
        return(
            f"Hola soy {self.nombre}, un {self.especie} y tengo {self.edad} años"
        )

#definicion del objeto
perro1 = Hoil("Dexter","Labrador",3)

print(perro1.presentar())

class Cuenta_Bancaria:
#Función del constructor/inicializador 
    def __init__(self,titular,saldo_inicial):
        #Atributos 
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    #Definicion de metodos 
    def consulta (self):
        return(
            f"Hola {self.titular}, su saldo es {self.saldo_inicial}"
            )

    def depositar(self, monto):
        if monto > 0:
            self.saldo_inicial += monto
            print(
                f"Deposito exitoso de ${monto}, saldo actual = {self.saldo_inicial}"
                )
        else:
            print("El saldo es menor a 0")



            

hoil = Cuenta_Bancaria("Angel","1000")
print(hoil.consulta())



