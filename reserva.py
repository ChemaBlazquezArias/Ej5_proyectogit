import personas as p 
import cancha as c 
class Reserva:
    def __init__(self, numero, fecha, cliente, cancha, costo):
        self.numero = numero
        self.fecha = fecha
        self.cliente = cliente
        self.cancha = cancha
        self.costo = costo

    def crear_reserva(self):
        numero = int(input("Introduce el numero de la reserva: "))
             
        cliente = int(input("Introduce el nombre del cliente: "))
        if cliente not in p.lista_clientes:
            print("Cliente no está activo.")
        
        else:
        
            if cliente.saldo < -2000:
                print("Cliente tiene saldo negativo menor a -2000.")
                return False
            else:
                costo = int(input("Introduce el costo: "))
                cliente.saldo - costo
        
            fecha = int(input("Introduce la fecha: "))
            for fecha in c.lista_cachas:
                if fecha == c.lista_canchas.fecha:
                    print("Cancha ocupada en ese horario.")
                    return False

            cancha = int(input("Introduce el nombre de la cancha: "))
            if cancha not in c.lista_canchas:
                print("Cancha no existe.")
                return False

        nueva_reserva = Reserva(numero, fecha, cliente, cancha, costo)
        return nueva_reserva

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


