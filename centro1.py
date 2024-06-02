import personas as p 
import cancha as c 
import reserva as r

class Centro:
    def __init__(self, nombre_centro, direccion_centro):
        self.nombre_centro = nombre_centro
        self.direccion_centro = direccion_centro
        
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
                print("3. Mostrar información.")
                print("4. Buscar cancha (por deporte).")
                print("5. Mostrar canchas reservadas.")
                print("6. Mostrar cliente y reserva.")
                print("7. Eliminar cancha.")
                print("8. Atrás.")
                opcion_centro = int(input("Selecciona una opción: "))
                
                while True:
                    
                    if opcion_centro == 1:
                        centro = Centro.crear_centro()
                        print("Ya tenemos centro.")
                        print(centro)
                        
                    elif opcion_centro == 2:
                        nueva_cancha = c.agregar_cancha()
                        lista_canchas.append(nueva_cancha)
                        print("¡La nueva cancha se ha creado con exito!")
                        print(nueva_cancha)

                    elif opcion_centro == 3:
                        print(f"{centro.nombre_centro} Dirección: {centro.direccion_centro}")
                        for i, cancha in enumerate(lista_canchas):
                            print(f"Cancha número: {cancha.numero} Deporte: {cancha.deporte} ")
                    
                    elif opcion_centro == 4:
                        c.listar_canchas_por_deporte()
                    
                    elif opcion_centro == 5:
                        canchas_reservadas = c.mostrar_canchas_reservadas()
                        print(f"Las canchas reservadas son:\n{canchas_reservadas}")
                    
                    elif opcion_centro == 6: 
                        print(r.listar_reservas_cliente())
                    
                    elif opcion_centro == 7:
                        c.quitar_cancha(lista_canchas)

                    elif opcion_centro == 8:
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
                    
                    elif opcion_empleados == 2:
                        for i, nuevo_empleado in enumerate(lista_empleados):
                            print(f"{i+1}. {nuevo_empleado}")
                    
                    elif opcion_empleados == 3:
                        nueva_tarea = p.asignar_tarea()
                        print(nueva_tarea)
                    
                    elif opcion_empleados == 4:
                        p.eliminar_tarea_empleado()
                    
                    elif opcion_empleados == 5:
                        print("Volviendo al menú principal...")
                        break
                
            elif opcion == 3:
                print("--Menú de la gestión de los clientes--")
                print("1. Añadir un cliente.")
                print("2. Añadir saldo a un cliente.")
                print("3. Mostrar saldo de un cliente.")
                print("4. Ver lista de clientes del centro.")
                print("5. Mostrar lista de clientes morosos.")
                print("6. Dar de baja a un cliente.")
                print("7. crear reserva.")
                print("8. Atrás.")
                opcion_clientes = int(input("Selecciona una opción: "))
                
                while True:
                    """Encarna aqui he tenido un problemilla y es que me aparecia hecho por mi, cuando lo habia
                    hecho chema, lo he borrado para decirle que lo hiciese y ahora no puede, 
                    intenta no tener en cuenta que salga mi nombre"""
                    if opcion_clientes == 1: # hecho por Chema
                        nuevo_cliente = p.crear_cliente()
                        lista_clientes.append(nuevo_cliente)
                        print("¡Cliente creado con éxito!")
                        print(nuevo_cliente)
                        break

                    elif opcion_clientes == 2:
                        nuevo_saldo = p.introducir_saldo(nuevo_cliente, lista_clientes)
                        print(nuevo_saldo)
                    
                    elif opcion_clientes == 3:
                        saldo_cliente = p.mostrar_saldo(nuevo_cliente, lista_clientes)
                        print(saldo_cliente)
                    
                    elif opcion_clientes == 4: 
                        for i, cliente in enumerate(lista_clientes):
                            print(f"{i+1}. {cliente.nombre} {cliente.apellido} Id cliente: {cliente.identificador}")
                    
                    elif opcion_clientes == 5: 
                        nuevo_moroso = p.cliente_moroso(nuevo_cliente, lista_morosos)
                        mostrar_moroso = p.mostrar_morosos(nuevo_moroso, lista_morosos)
                        print(mostrar_moroso) 
                    
                    elif opcion_clientes == 6: 
                         p.eliminar_cliente(lista_clientes)        
                    
                    elif opcion_clientes == 7: 
                        nueva_reserva = r.crear_reserva()
                        print(nueva_reserva)
                    
                    elif opcion_clientes == 8:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 4:
                print("Saliendo del programa...\n"
                      "¡Hasta pronto!")
                break
    
    main()