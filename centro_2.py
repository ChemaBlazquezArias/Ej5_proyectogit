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
    lista_reservas = []
    
    while True:
        print("1. Gestionar Centro.")
        print("2. Gestionar Empleados.")
        print("3. Gestionar Clientes.")
        print("4. Salir.")
        try: 
            opcion = int(input("¿Qué quieres hacer? "))
        
            if opcion == 1:
                print("--Menú de la gestión del centro--")
                print("1. Crear centro.")
                print("2. Crear cancha.") # Enrique 
                print("3. Mostrar información y canchas.")
                print("4. Buscar cancha (por deporte).")
                print("5. Mostrar canchas reservadas.")
                print("6. Mostrar reservas.")
                print("7. Eliminar cancha.")
                print("8. Atrás.")
                opcion_centro = int(input("Selecciona una opción: "))
                while True:
                    if opcion_centro == 1:
                        mi_centro = crear_centro()
                        print("--Centro creado con éxito--")
                        print(f"{mi_centro.nombre_centro} Dirección: {mi_centro.direccion_centro}")
                        break
                    
                    elif opcion_centro == 2:
                        nueva_cancha = c.Cancha.agregar_cancha()
                        lista_canchas.append(nueva_cancha)
                        print(nueva_cancha)
                        break
                                
                    elif opcion_centro == 3:
                        print(f"{mi_centro.nombre_centro} Dirección: {mi_centro.direccion_centro}")
                        for i, cancha in enumerate(lista_canchas):
                            print(f"Cancha número: {cancha.numero} Deporte: {cancha.deporte} ")
                        break
                    
                    elif opcion_centro == 4:
                        canchas_filtro = c.Cancha.listar_canchas_por_deporte()
                        print(canchas_filtro)
                        break
                    
                    elif opcion_centro == 5:
                        r.Reserva.listar_reservas_cancha(cancha)
                        break
                    
                    elif opcion_centro == 6:
                        p.mostrar_reservas(cliente)
                        break
                    
                    elif opcion_centro == 7:
                        c.Cancha.quitar_cancha(cancha)
                        break
                    
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
                        break
                    
                    elif opcion_empleados == 2:
                        for i, nuevo_empleado in enumerate(lista_empleados):
                            print(f"{i+1}. {nuevo_empleado}")
                        break
                    
                    elif opcion_empleados == 3:
                        nueva_tarea = p.asignar_tarea()
                        print(nueva_tarea)
                        break
            
                    elif opcion_empleados == 4: 
                        eliminar_empleado = p.eliminar_tarea_empleado()
                        print(eliminar_empleado)
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
                print("5. Mostrar lista de clientes morosos.")
                print("6. Dar de baja a un cliente.")
                print("7. Realizar reserva.")
                print("8. Atrás.")
                opcion_clientes = int(input("Selecciona una opción: "))
                while True:
                    if opcion_clientes == 1:
                        nuevo_cliente = p.crear_cliente()
                        lista_clientes.append(nuevo_cliente)
                        print("¡Cliente creado con éxito!")
                        print(nuevo_cliente)
                        break
                    
                    elif opcion_clientes == 2:
                        nuevo_saldo = p.introducir_saldo(nuevo_cliente, lista_clientes)
                        print(nuevo_saldo)
                        break
                    
                    elif opcion_clientes == 3:
                        saldo_cliente = p.mostrar_saldo(nuevo_cliente, lista_clientes)
                        print(saldo_cliente)
                        break
                    
                    elif opcion_clientes == 4:
                        print("--Lista de clientes del Centro--")
                        for i, cliente in enumerate(lista_clientes):
                            print(f"{i+1}. {cliente.nombre} {cliente.apellido} Id cliente: {cliente.identificador}")
                        break
                    
                    elif opcion_clientes == 5:
                        nuevo_moroso = p.cliente_moroso(nuevo_cliente, lista_morosos)
                        mostrar_moroso = p.mostrar_morosos(nuevo_moroso, lista_morosos)
                        print(mostrar_moroso)
                        break
                    
                    elif opcion_clientes == 6:
                        p.eliminar_cliente(lista_clientes)
                        break
                    
                    elif opcion_clientes == 7:
                        nombre = input("Nombre: ")
                        id_cliente = input("Ingrese el ID del cliente: ")
                        id_pista = input("Ingrese el ID de la pista: ")
                        deporte = input("Ingrese el deporte: ")
                        fecha = input("Ingrese la fecha (YYYY-MM-DD HH:MM): ")
                        precio = float(input("Ingrese el precio de la reserva: "))
                        nueva_reserva = p.reservar_cancha(nombre, id_cliente, id_pista, deporte, fecha, precio)
                        lista_reservas.append(nueva_reserva)
                        print("¡Cancha reservada con éxito!")
                        break
                        
                    elif opcion_clientes == 9:
                        print("Volviendo al menú principal...")
                        break
                    
            elif opcion == 4:
                print("Saliendo del programa...\n"
                        "¡Hasta pronto!")
                break
        
        except ValueError as err:
            print("Error: ", err)
main()
        

        