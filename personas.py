class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, identificador, activo, saldo):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
        self.saldo = saldo
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} Teléfono: {self.telefono} Identificador: {self.identificador} Activo: {self.activo} Saldo: {self.saldo} €."

lista_clientes = []
lista_empleados = []
       
def crear_cliente():
    cliente_temporal = datos_comunes()
    telefono = int(input("Teléfono: "))
    identificador = int(input("Identificador: "))
    activo = str(input("Activo (S/N): ")).lower() == 's' # cliente activo o en vez de darse de baja dejarlo como cliente inactivo
    saldo = float(input("Saldo: "))
    return Cliente(cliente_temporal.nombre, cliente_temporal.apellido, telefono, identificador, activo, saldo)

def agregar_cliente(): # añadir el cliente en la lista del centro
    cliente_temporal = crear_cliente()
    lista_clientes.append(cliente_temporal)

def introducir_saldo(cliente, lista_clientes):
    for i, cliente in enumerate(lista_clientes):
        print(f"{i + 1}. {cliente}")
    cliente_saldo = int(input("Cliente que desea añadir saldo a su cuenta: ")) - 1
    if 0 <= cliente_saldo < len(lista_clientes):
        nuevo_saldo = float(input("Cantidad: "))
        cliente.saldo += nuevo_saldo
        print(f"El cliente {cliente.nombre} {cliente.apellido}, con identificador {cliente.identificador} ha añadido a su saldo {nuevo_saldo} € Total saldo: {cliente.saldo} €.")
    else: 
        print("Selecciona un número válido.")

def mostrar_saldo(cliente, lista_clientes):
    for i, cliente in enumerate(lista_clientes):
        print(f"{i + 1}. {cliente}")
    ver_saldo = int(input("Cliente que desea ver el saldo de su cuenta: ")) - 1
    if 0 <= ver_saldo < len(lista_clientes):
        print(f"El cliente {cliente.nombre} {cliente.apellido}, con identificador {cliente.identificador} tiene en su cuenta {cliente.saldo} €.")
    else: 
        print("Selecciona un número válido.")
        
def eliminar_cliente(lista_clientes): # valorar el poder eliminar al cliente con el identificador, REVISAR
    if lista_clientes: 
        for i, cliente in enumerate(lista_clientes):
            print(f"{i + 1}. {cliente}")
        eliminar_cliente = int(input("¿Qué cliente deseas eliminar?")) - 1
        if 0 <= eliminar_cliente < len(lista_clientes):
            lista_clientes.pop(eliminar_cliente)
            print("--Cliente eliminado--")
        else:
            print("Selecciona un número válido.")
    else:
        print("No hay clientes en la lista.")
            
def cliente_moroso(cliente, lista_clientes): # añadir a la lista total de morosos revisar
    lista_morosos = []
    for cliente in lista_clientes:
        if cliente.saldo < -2000:
            lista_morosos.append(cliente)
    return lista_morosos

def mostrar_morosos(cliente, lista_morosos): 
    if lista_morosos:
        for i, cliente in enumerate(lista_morosos):
            print(f"{i + 1}. {cliente}")
             
class Empleados(Persona):
    def __init__(self, nombre, apellido, desocupado, lista_tareas):
        super().__init__(nombre, apellido)
        self.desocupado = desocupado
        self.lista_tareas = lista_tareas
        
    def __str__(self):
        return f"Empleado: {self.nombre} {self.apellido} Desocupado: {self.desocupado} LISTA DE TAREAS: {self.lista_tareas}"
        

def crear_empleado(): # registrar un empleado 
    empleado_temporal = datos_comunes()
    desocupado = str(input("Desocupado (S/N): ")).lower() == 's'
    lista_tareas_input = str(input("Asignar tarea (separar tareas por comas): "))
    lista_tareas = [tarea.strip() for tarea in lista_tareas_input.split(',')]  # Convertir la cadena en una lista
    return Empleados(empleado_temporal.nombre, empleado_temporal.apellido, desocupado, lista_tareas)

def asignar_empleado(): # asignar un empleado a una cancha
    empleado_temporal = crear_empleado()
    lista_empleados.append(empleado_temporal)
    
def asignar_tarea():
    if not lista_empleados:
        print("No hay empleados registrados.")
        return

    for i, empleado_temporal in enumerate(lista_empleados):
        print(f"{i+1}. {empleado_temporal}")
    
    try:
        empleado_tarea = int(input("Indique el número del empleado al que quiere asignar una tarea: "))
        if 1 <= empleado_tarea <= len(lista_empleados):
            tarea_pendiente = str(input("Tarea: "))
            lista_empleados[empleado_tarea - 1].agregar_tarea(tarea_pendiente)
            print(f"Tarea '{tarea_pendiente}' asignada a {lista_empleados[empleado_tarea - 1]}")
        else:
            print("Número de empleado no válido.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")

def eliminar_tarea_empleado():
    if not lista_empleados:
        print("No hay empleados registrados.")
        return
    
    for i, empleado in enumerate(lista_empleados):
        print(f"{i+1}. {empleado}")
    
    try:
        empleado_indice = int(input("Indique el número del empleado del que quiere eliminar una tarea: ")) - 1
        if 0 <= empleado_indice < len(lista_empleados):
            empleado = lista_empleados[empleado_indice]
            if not empleado.lista_tareas:
                print(f"El empleado {empleado.nombre} {empleado.apellido} no tiene tareas asignadas.")
                return

            for t, tarea in enumerate(empleado.lista_tareas):
                print(f"{t+1}. {tarea}")
            
            tarea_indice = int(input("Indique el número de la tarea que desea eliminar: ")) - 1
            if 0 <= tarea_indice < len(empleado.lista_tareas):
                tarea_eliminada = empleado.lista_tareas[tarea_indice]
                empleado.eliminar_tarea(tarea_eliminada)
                print(f"Tarea '{tarea_eliminada}' eliminada del empleado {empleado.nombre} {empleado.apellido}.")
            else:
                print("Número de tarea no válido.")
        else:
            print("Número de empleado no válido.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
         
def empleados_desocupados():
    personal_desocupado = []  # Crear una lista vacía para los empleados desocupados
    for empleado in lista_empleados: 
        if empleado.desocupado:
            personal_desocupado.append(empleado)

    if personal_desocupado:
        print("--Lista de empleados desocupados--")
        for i, empleado in enumerate(personal_desocupado):
            print(f"{i+1}. {empleado.nombre} {empleado.apellido}")
    else:
        print("No hay empleados desocupados.")

def eliminar_empleado_cancha():
    lista_canchas = []
    
    if not lista_canchas:
        print("No hay canchas registradas.")
        return

    for i, cancha in enumerate(lista_canchas):
        print(f"{i+1}. {cancha}")
    
    try:
        cancha_indice = int(input("Indique el número de la cancha de la que quiere eliminar un empleado: ")) - 1
        if 0 <= cancha_indice < len(lista_canchas):
            cancha = lista_canchas[cancha_indice]
            if not cancha.empleados_asignados:
                print(f"La cancha {cancha.nombre} no tiene empleados asignados.")
                return

            for e, empleado in enumerate(cancha.empleados_asignados):
                print(f"{e+1}. {empleado.nombre} {empleado.apellido}")
            
            empleado_indice = int(input("Indique el número del empleado que desea eliminar: ")) - 1
            if 0 <= empleado_indice < len(cancha.empleados_asignados):
                empleado_eliminado = cancha.empleados_asignados[empleado_indice]
                cancha.eliminar_empleado(empleado_eliminado)
                print(f"Empleado '{empleado_eliminado.nombre} {empleado_eliminado.apellido}' eliminado de la cancha {cancha.nombre}.")
            else:
                print("Número de empleado no válido.")
        else:
            print("Número de cancha no válido.")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")

def datos_comunes():
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    return Persona(nombre, apellido)