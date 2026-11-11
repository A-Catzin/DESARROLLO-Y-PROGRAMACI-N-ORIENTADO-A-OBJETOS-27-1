class Personaje:
    def atacar(self):
        print("El personaje realiza un ataque básico")


class Arquero(Personaje):
    def atacar(self):
        print("Arquero: Dispara una flecha a distancia")


class Mago(Personaje):
    def atacar(self):
        print("Mago: Lanza una bola de fuego")


class Guerrero(Personaje):
    def atacar(self):
        print("Guerrero: Golpea con la espada")


equipo = [Arquero(), Mago(), Guerrero()]

for personaje in equipo:
    personaje.atacar()