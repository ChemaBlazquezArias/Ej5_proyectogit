class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono, identificador, activo):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.identificador = identificador
        self.activo = activo
        
def crear_cliente():
    cliente_temporal = datos_comunes()
    telefono = int(input("Teléfono: "))
    identificador = int(input("Identificador: "))
    activo = str(input("Activo (S/N): ")).lower == 's' # cliente activo o en vez de darse de baja dejarlo como cliente inactivo
    return Cliente(cliente_temporal.nombre, cliente_temporal.apellido, telefono, identificador, activo)

def agregar_cliente(): # añadir el cliente en la lista del centro
    pass

def eliminar_cliente(lista): # valorar el poder eliminar al cliente con el identificador, REVISAR
    if lista: 
        for i, cliente in enumerate(lista):
            print(f"{i + 1}. {cliente}")
        eliminar_cliente = int(input("¿Qué cliente deseas eliminar?")) - 1
        if 0 <= eliminar_cliente < len(lista):
            lista.pop(eliminar_cliente)
            print("--Cliente eliminado--")
        else:
            print("Selecciona un número válido.")
    else:
        print("No hay clientes en la lista.")
            

def cliente_moroso():
    pass
                
class Empleados(Persona):
    def __init__(self, nombre, apellido, desocupado, lista_tareas):
        super().__init__(nombre, apellido)
        self.desocupado = desocupado
        self.lista_tareas = lista_tareas

def agregar_empleado(): # registrar un empleado a una cancha
    empleado_temporal = datos_comunes()
    desocupado = str(input("Desocupado (S/N): ")).lower == 's'
    lista_tareas = str(input("Asignar tarea: "))
    return Empleados(empleado_temporal.nombre, empleado_temporal.apellido, desocupado, lista_tareas)

def asignar_tarea():
    pass

def empleados_desocupados():
    pass

def eliminar_empleado_cancha():
    pass

def datos_comunes():
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    return Persona(nombre, apellido)
     