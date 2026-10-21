#Variable
Precio_Producto = 50
#Contante
IVA = 1.6

#Operacion
Total = (Precio_Producto * IVA)
print(Total)


Saldo = 500
retiro = 200

Puede_Retirar = (Saldo - retiro) >= 0
print("Puede retirar", Puede_Retirar)


Calificacion = 8

if Calificacion >= 6:
    print("Aprovado")
else:
    print("Reprobado")


for i in range(1,4):
    print("Numero", i)

Frutas =  ["Manzana","Pera","Platano",]
print(Frutas[0])

def lol (a,b):
    return(a+b)
resultado = lol(2,3)
print("La suma es", resultado)



#Declara una cons llamada bono puntualidad con un valor de 500, declara variables para el nombre de un empleado, su sueldo base y los dias faltados en el mes 
#Escribe la logica para calcular su pago final restandole 100 pesos por cada dia faltado y sumandole el bono de puntualidad
Nom = "Hoil"

def pagos (Dias_Faltado):
    Resta= 100*Dias_Faltado
    Sueldo = 1500
    if Dias_Faltado == 0:
        Sueldo += 500
    else:
        Sueldo -= Resta
    return Sueldo

    

pago = pagos(0)
print("El pago de ", Nom,"es: ", pago)

#Simula el registro de la venta de un boleto de cine debes declarar e inicializar variables de 4 tipos de datos distintos titulo/Text, Edad/int, Precio/Float y Funcion_3D/boolean
#Imprime un ticket convinando todos estos datos en una frase

Titulo = "Tilin"
Edad = 67
Precio= 9.67
Function_3D= True

print("Boleto comprado para:", Titulo,"Con precio de:", Precio, "Para edades recomendadas de:", Edad, "Es 3d?",Function_3D)

#A partir de una varia1ble numerica que almacene una calificacion del 0 al 100 utiliza una estructura condicional anidada para asignar y mostrar una categoria de desempeño
# 100-90 excelente, 89-80 bueno,79-70, <70 Reprobado, comprobar el numero si es mayor a 100 o menor a 0

Calificacion = 85

if Calificacion < 0 or Calificacion > 100:
    print("Calificacion no valida")
else:
    if Calificacion >= 90:
        Categoria = "Excelente"
    else:
        if Calificacion >= 80:
            Categoria = "Bueno"
        else:
            if Calificacion >= 70:
                Categoria = "Regular"
            else:
                Categoria = "Reprobado"

    print("La calificacion es:", Calificacion, "Categoria:", Categoria)


#Montaña rusa w
altura = 150
edad = 18
pase_vip = True

if (altura > 140 and edad >= 12) or pase_vip:
    print("SI permitira el acceso.")
else:
    print("NO permitira el acceso.")


#Funcion para calcular el IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Bajo peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"
    return imc, categoria

peso = 70
altura = 1.75
imc, categoria = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f} y tu categoria es: {categoria}")