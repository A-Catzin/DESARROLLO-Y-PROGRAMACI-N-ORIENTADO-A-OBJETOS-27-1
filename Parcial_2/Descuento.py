class cal_desc:
    def __init__(self, subtotal):
        self.subtotal = subtotal

    def __add__(self, descuento):
        descuento = self.subtotal * 0.10

        if self.subtotal >= 1000:
            return self.subtotal - descuento
        else:
            return self.subtotal

compra = cal_desc(1000)
print (f"El total después del descuento es: ${compra + 0}")