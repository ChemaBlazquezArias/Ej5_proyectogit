class Cancha:
    lista_canchas = []
    
    def __init__(self, numero, deporte, precio, habilitada):
        self.numero = numero
        self.deporte = deporte
        self.precio = precio
        self.habilitada = habilitada
        self.reservas = []

    def __str__(self):
        return f"Cancha(numero={self.numero}, deporte={self.deporte}, precio={self.precio}, habilitada={self.habilitada})"

    @classmethod
    def agregar_cancha(cls): #Se debe añadir el cls igual que el abc en el abstract
        numero = int(input("Introduce el número de la cancha: "))
        for cancha in cls.lista_canchas:
            if cancha.numero == numero:
                print(f"La cancha número {numero} ya está registrada.")
                return
        deporte = input("Introduce el deporte que se practica en la cancha: ")
        precio = float(input("Introduce el precio de alquiler de la cancha: "))
        habilitada = input("¿Está habilitada la cancha? (si/no): ").strip().lower() == 'si'
        nueva_cancha = cls(numero, deporte, precio, habilitada)
        cls.lista_canchas.append(nueva_cancha)
        print(f"Cancha número {numero} agregada correctamente.")
        
    @classmethod
    def listar_canchas_por_deporte(cls, deporte):
        canchas_filtradas = [cancha for cancha in cls.lista_canchas if cancha.deporte == deporte]
        if canchas_filtradas:
            for cancha in canchas_filtradas:
                print(cancha)
        else:
            print(f"No se encontraron canchas para el deporte: {deporte}")

    @classmethod
    def quitar_cancha(cls, numero):
        numero = int(input("Introduce el numero de la cancha: "))
        for cancha in cls.lista_canchas:
            if cancha.numero == numero:
                if cancha.habilitada == 'si':
                    print ("La cancha está en uso y no se puede eliminar.")
                    break
                
                else:
                    if cancha.numero == numero:
                        cls.lista_canchas.remove(cancha)
                        print(f"Cancha con número {numero} eliminada.\n")
                        break
        else:
            print(f"No se encontró una cancha con el número {numero}.")
    
        
        
