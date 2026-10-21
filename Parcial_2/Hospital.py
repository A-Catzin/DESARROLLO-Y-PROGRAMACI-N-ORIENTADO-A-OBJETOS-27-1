class Paciente:
    def __init__(self, numero_seguro_social, tipo_sangre, peso_kg):
        self.__numero_seguro_social = numero_seguro_social  # Atributo privado
        self.__tipo_sangre = tipo_sangre                    # Atributo privado
        self.__peso_kg = peso_kg                            # Atributo privado

    # 1. Get y Set tradicionales (numero_seguro_social)
    def get_numero_seguro_social(self):
        return self.__numero_seguro_social

    def set_numero_seguro_social(self, nuevo_nss):
        self.__numero_seguro_social = nuevo_nss

    # 2. Get y Set tradicionales (tipo_sangre)
    def get_tipo_sangre(self):
        return self.__tipo_sangre

    def set_tipo_sangre(self, nuevo_tipo):
        self.__tipo_sangre = nuevo_tipo


class Doctor:
    def __init__(self, cedula_profesional, especialidad, disponible=True):
        self.__cedula_profesional = cedula_profesional  # Atributo privado
        self.__especialidad = especialidad              # Atributo privado
        self.__disponible = disponible                  # Atributo privado

    # 1. Con @property y setter (cedula_profesional)
    @property
    def cedula_profesional(self):
        return self.__cedula_profesional

    @cedula_profesional.setter
    def cedula_profesional(self, nueva_cedula):
        self.__cedula_profesional = nueva_cedula

    # 2. Con @property y setter (especialidad)
    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        self.__especialidad = nueva_especialidad
