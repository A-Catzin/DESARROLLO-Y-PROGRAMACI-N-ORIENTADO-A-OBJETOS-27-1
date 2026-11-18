class figura:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return

class Rectangulo(figura):
    def area(self):
        return self.base * self.altura

class Triangulo(figura):
    def area(self):
        return (self.base * self.altura) / 2

class cuadrado(figura):
    def area(self):
        return self.base * self.base

fig = [Rectangulo(5, 10), Triangulo(4, 6), cuadrado(3, 3)]

for f in fig:
    print(f"El área de la figura es: {f.area()}")