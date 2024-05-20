class Reserva:
    def __init__(self, numero, fecha, cliente, cancha, costo):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
        self.costo = costo

    def crear_reserva(self, fecha, cliente, cancha, costo):
        if not cliente.activo:
            print("Cliente no está activo.")
            return False

        if cliente.saldo < -2000:
            print("Cliente tiene saldo negativo menor a -2000.")
            return False

        for reserva in cancha.habilitada:
            if reserva.fecha == fecha:
                print("Cancha ocupada en ese horario.")
                return False

        nueva_reserva = Reserva(self.numero, fecha, cliente, cancha, costo)
        self.numero += 1

        cliente.saldo -= costo
        cliente.reservas.append(nueva_reserva)
        cancha.reservas.append(nueva_reserva)

        print(f"Reserva creada: {nueva_reserva.numero}")
        return True

    def listar_reservas_cancha(self, cancha):#Canchas reservadas
        print(f"Reservas de la cancha {cancha.nombre}:")
        for reserva in cancha.reservas:
            print(f"Reserva {reserva.numero} - Fecha: {reserva.fecha} - Cliente: {reserva.cliente.nombre}")

    def listar_reservas_cliente(self, cliente):# CLientes con reserva
        print(f"Reservas de {cliente.nombre}:")
        for reserva in cliente.reservas:
            print(f"Reserva {reserva.numero} - Fecha: {reserva.fecha} - Cancha: {reserva.cancha.nombre}")

    def mostrar_saldo_cliente(self, cliente):
        print(f"Saldo de {cliente.nombre}: {cliente.saldo}")

    def registrar_pago_cliente(self, cliente, monto):
        cliente.saldo += monto
        print(f"Pago registrado. Nuevo saldo de {cliente.nombre}: {cliente.saldo}")


