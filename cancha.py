class Cancha:
    def __init__(self, numero, deporte, precio, habilitada=True):
        self.numero = numero
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []

    def __str__(self):
        return f"Cancha {self.numero} - Deporte: {self.deporte} - Precio: {self.precio} - Habilitada: {self.habilitada}"

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def quitar_reserva(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
