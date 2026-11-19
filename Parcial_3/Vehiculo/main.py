from class_vehiculo import vehiculo
#Angel Ricardo Teh Catzin

while True:
    try:
        auto1 = vehiculo("Chevy pop", 150)
        print(f"La tarifa actual del vehiculo es: {auto1.tarifa}")


        auto1.tarifa = int(input("Ingrese la nueva tarifa del vehiculo: "))
        print(f"Tarifa actualizada del vehiculo es: {auto1.tarifa}")
        break
    except:
        print("No se puede actualizar. por favor intente de nuevo")
        print("El sistema continua ejecutandose")
    else:
        print("La tarifa se actualizo correctamente")
    finally:
        print("Fin del programa")