class Cancha:
    def __init__(self, numero, deporte, precio, habilitada):
        self.numero = numero
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []

    def __repr__(self):
        return f"Cancha(numero={self.numero}, deporte={self.deporte}, precio={self.precio}, habilitada={self.habilitada})"

canchas = []

def agregar_cancha(cancha):
    if any(c.numero == cancha.numero for c in canchas):
        print(f"La cancha número {cancha.numero} ya está registrada.")
    else:
        canchas.append(cancha)
        print(f"Cancha número {cancha.numero} agregada correctamente.")

def listar_canchas_por_deporte(deporte):
    canchas_filtradas = [cancha for cancha in canchas if cancha.deporte == deporte]
    return canchas_filtradas

def quitar_cancha(numero):
    cancha_a_quitar = None
    for cancha in canchas:
        if cancha.numero == numero:
            cancha_a_quitar = cancha
            break
    
    if cancha_a_quitar:
        if cancha_a_quitar.reservas:
            print(f"No se puede quitar la cancha número {numero} porque tiene reservas pendientes.")
        else:
            canchas.remove(cancha_a_quitar)
            print(f"Cancha número {numero} quitada correctamente.")
    else:
        print(f"No se encontró la cancha número {numero}.")
