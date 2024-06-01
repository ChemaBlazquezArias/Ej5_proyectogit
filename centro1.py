import personas as p 
import cancha as c 
import reserva as r

class Centro:
    def crear_centro():
        nombre_centro = str(input("Nombre del centro: "))
        direccion_centro = str(input("Dirección del centro: "))
        return Centro(nombre_centro, direccion_centro)
    
    @staticmethod
    def main():
        
        lista_canchas = []
        lista_clientes = []
        lista_empleados = []
        lista_morosos = []
        lista_centro = []
        
        while True:
            print("1. Gestionar Centro.")
            print("2. Gestionar Empleados.")
            print("3. Gestionar Clientes.")
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
                        nueva_cancha = c.agregar_cancha()
                        lista_canchas.append(nueva_cancha)
                        print("¡La nueva cancha se ha creado con exito!")
                        print(nueva_cancha)
                        
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
                print("3. Asignar tarea a un empleado.")
                print("4. Quitar tarea a un empleado.")
                print("5. Atrás.")
                opcion_empleados = int(input("Selecciona una opción: "))
                
                while True:
                    
                    if opcion_empleados == 1:
                        nuevo_empleado = p.crear_empleado()
                        lista_empleados.append(nuevo_empleado)
                        print("¡Empleado añadido con éxito!")
                        print(nuevo_empleado)
                        break
                    
                    elif opcion_empleados == 2:
                        for i, nuevo_empleado in enumerate(lista_empleados):
                            print(f"{i+1}. {nuevo_empleado}")
                        break
                    
                    elif opcion_empleados == 3: # revisar
                        p.asignar_tarea()
            
                        break
                    elif opcion_empleados == 4: # revisar
                        p.eliminar_tarea_empleado()
                        break
                    
                    elif opcion_empleados == 5:
                        print("Volviendo al menú principal...")
                        break
                
            elif opcion == 3:
                print("--Menú de la gestión de los clientes--")
                print("1. Añadir un cliente.")
                print("2. Añadir saldo a un cliente.")
                print("3. Mostrar saldo de un cliente.")
                print("4. Ver lista de clientes del centro.")
                print("5. Anular una reserva.")
                print("6. Mostrar lista de clientes morosos.")
                print("7. Dar de baja a un cliente.")
                print("8. Atrás.")
                opcion_clientes = int(input("Selecciona una opción: "))
                while True:
                    if opcion_clientes == 1: # hecho por Chema
                       
                        break
                    
                    elif opcion_clientes == 2:
                        nuevo_saldo = p.introducir_saldo(nuevo_cliente, lista_clientes)
                        print(nuevo_saldo)
                        break
                    
                    elif opcion_clientes == 3:
                        saldo_cliente = p.mostrar_saldo(nuevo_cliente, lista_clientes)
                        print(saldo_cliente)
                        break
                    
                    elif opcion_clientes == 4: # lista clientes del centro(lista centro)
                        pass
                    
                    elif opcion_clientes == 5: # anular una reserva
                        pass
                    
                    elif opcion_clientes == 6: # lista de morosos (no sale nada, REVISAR)
                        nuevo_moroso = p.cliente_moroso(nuevo_cliente, lista_morosos)
                        print(nuevo_moroso)
                        break
                    
                    elif opcion_clientes == 7: # dar de baja a un cliente 
                        pass
                    elif opcion_clientes == 8:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 4:
                print("Saliendo del programa...\n"
                      "¡Hasta pronto!")
                break
    
    main()