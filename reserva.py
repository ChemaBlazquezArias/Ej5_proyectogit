class Reserva:
    def __init__(self, numero, fecha, cliente, cancha):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha

    def __str__(self):
        return f"Reserva {self.numero} - Fecha: {self.fecha} - Cliente: {self.cliente.DNI} - Cancha: {self.cancha.numero}"

class Cliente:
    def __init__(self, DNI, nombre, saldo=0):
        self.DNI = DNI
        self.nombre = nombre
        self.saldo = saldo

    def __str__(self):
        return f"DNI: {self.DNI} - Cliente: {self.nombre} - Saldo: {self.saldo}"

    def reservar(self, reserva):
        if self.saldo < 0:
            print("No puedes reservar, saldo insuficiente.")
            return False
        self.saldo -= reserva.cancha.precio
        reserva.cancha
        print("Reserva realizada con éxito.")
        return True

    def realizar_pago(self, cantidad):
        self.saldo += cantidad
        print(f"Se ha registrado un pago de {cantidad} para el cliente {self.nombre}.")

    def mostrar_saldo(self):
        print(f"El saldo actual de {self.nombre} es: {self.saldo}")

