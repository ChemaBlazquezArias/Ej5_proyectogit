class Centro:
    def crear_centro():
        nombre_centro = str(input("Nombre del centro: "))
        direccion_centro = str(input("Dirección del centro: "))
        return Centro(nombre_centro, direccion_centro)
    
    @staticmethod
    def main():
        
        lista_canchas = []
        lista_clientes = []
        
        while True:
            print("1. Gestionar Centro.")
            print("2. Gestionar Clientes.")
            print("3. Gestionar Empleados.")
            print("4. Salir.")
            opcion = int(input("¿Qué quieres hacer? "))
            
            if opcion == 1:
                print("--Menú de la gestión del centro--")
                print("1. Crear centro.")
                print("2. Crear cancha.")
                print("3. Mostrar canchas.")
                print("4. Mostrar información.")
                print("5. Buscar cancha (por deporte).")
                print("6. Mostrar canchas reservadas.")
                print("7. Mostrar cliente y reserva.")
                print("8. Eliminar cancha.")
                print("9. Atrás.")
                opcion_centro = int(input("Selecciona una opción: "))
                while True:
                    if opcion_centro == 1:
                        pass
                    elif opcion_centro == 2:
                        pass
                    elif opcion_centro == 3:
                        pass
                    elif opcion_centro == 4:
                        pass
                    elif opcion_centro == 5:
                        pass
                    elif opcion_centro == 6:
                        pass
                    elif opcion_centro == 7:
                        pass
                    elif opcion_centro == 8:
                        pass
                    elif opcion_centro == 9:
                        print("Volviendo al menú principal...")
                        break
                
            elif opcion == 2:
                print("--Menú de la gestión de los empleados--")
                print("1. Añadir empleado.")
                print("2. Mostrar lista de empleados.")
                print("3. Asignar tarea a un empleado.s")
                print("4. Quitar tarea a un empleado.")
                print("5. Atrás.")
                opcion_empleados = int(input("Selecciona una opción: "))
                while True:
                    if opcion_empleados == 1:
                        pass
                    elif opcion_empleados == 2:
                        pass
                    elif opcion_empleados == 3:
                        pass
                    elif opcion_empleados == 4:
                        pass
                    elif opcion_empleados == 5:
                        print("Volviendo al menú principal...")
                        break
                
            elif opcion == 3:
                print("--Menú de la gestión de los clientes--")
                print("1. Añadir un cliente.")
                print("2. Añadir saldo a un cliente.")
                print("3. Mostrar saldo de un cliente.")
                print("4. Anular una reserva.")
                print("5. Mostrar lista de clientes morosos.")
                print("6. Dar de baja a un cliente.")
                print("7. Atrás.")
                opcion_clientes = int(input("Selecciona una opción: "))
                while True:
                    if opcion_clientes == 1:
                        pass
                    elif opcion_clientes == 2:
                        pass
                    elif opcion_clientes == 3:
                        pass
                    elif opcion_clientes == 4:
                        pass
                    elif opcion_clientes == 5:
                        pass
                    elif opcion_clientes == 6:
                        pass
                    elif opcion_clientes == 7:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 4:
                print("Saliendo del programa...\n"
                      "¡Hasta pronto!")
                break
    
    main()
        

        