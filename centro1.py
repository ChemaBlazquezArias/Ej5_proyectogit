class Centro:
    def crear_centro():
        nombre_centro = str(input("Nombre del centro: "))
        direccion_centro = str(input("Direccion del centro: "))
        lista_canchas = []
        lista_clientes = []
        print(nombre_centro)
        print(direccion_centro)
        
    @staticmethod
    def main():
        lista_canchas = []
        lista_clientes = []
        
        while True:
            print("1. Gestionar Centro.")
            print("2. Gestionar Clientes.")
            print("3. Gestionar Empleados.")
            opcion = int(input("¿Qué quieres hacer? "))
            
            if opcion == 1:
                print("Dirigiendose a centro, por favor espere... ")
                while True:
                    print(" --Submenu de Centro--")
                    print("1. Crear centro.")
                    print("2. Crear cancha")
                    print("3. Mostrar canchas")
                    print("4. Mostar informacion")
                    print("5. Buscar cancha(por deporte)")
                    print("6. Mostrar canchas reservadas.")
                    print("7. Mostrar cliente y reserva.")
                    print("8. Eliminar cancha.")
                    print("9. Atras.")
                    opcion_centro = int(input("Introduce tu eleccion: "))
                    
                    if opcion_centro == 1:
                        pass
                    elif opcion_centro == 9:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 2:
                print("Dirigiendose a clientes, por favor espere... ")
                while True:
                    print(" --Submenu de Clientes--")
                    print("1. ")
                    print("2. Añadir saldo")
                    print("3. Hacer reserva")
                    print("4. Cancelar reserva")
                    print("5. Eliminar cliente.")
                    print("6. Atras.")
                    opcion_centro = int(input("Introduce tu eleccion: "))
                    
                    if opcion_centro == 1:
                        pass
                    elif opcion_centro == 6:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 3:
                print("Dirigiendose a empleados, por favor espere... ")
                while True:
                    print(" --Submenu de Empleados--")
                    print("1. Crear Empleado.")
                    print("2. Añadir tarea a Empleado")
                    print("3. Mostrar Empleados con tarea")
                    print("4. Eliminar tarea")
                    print("5. Atras.")
                    opcion_centro = int(input("Introduce tu eleccion: "))
                    
                    if opcion_centro == 1:
                        pass
                    elif opcion_centro == 5:
                        print("Volviendo al menú principal...")
                        break

Centro.main()