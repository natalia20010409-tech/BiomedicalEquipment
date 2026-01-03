from datetime import datetime

equipos = []

def registrar_equipo():
    nombre = input("Nombre del equipo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio_inicio = int(input("Año de inicio de operación: "))
    equipo = {
        "nombre": nombre,
        "marca": marca,
        "modelo": modelo,
        "anio_inicio": anio_inicio
    }
    equipos.append(equipo)
    print("Equipo registrado correctamente\n")
def calcular_antiguedad(anio_inicio):
    anio_actual = datetime.now().year
    return anio_actual - anio_inicio  
def evaluar_estado(antiguedad):
    if antiguedad >= 8:
        return "Requiere verificación"
    else:
        return "Operativo"
def listar_equipos():
    if not equipos:
        print("No hay equipos registrados\n")
        return
    print("\n LISTA DE EQUIPOS BIOMÉDICOS\n")
    for i, equipo in enumerate(equipos, start=1):
        antiguedad = calcular_antiguedad(equipo["anio_inicio"])
        estado = evaluar_estado(antiguedad)
        print(f"Equipo #{i}")
        print(f"Nombre: {equipo['nombre']}")
        print(f"Marca: {equipo['marca']}")
        print(f"Modelo: {equipo['modelo']}")
        print(f"Año de inicio: {equipo['anio_inicio']}")
        print(f"Antigüedad: {antiguedad} años")
        print(f"Estado: {estado}")
        print("-" * 30)
    print()
def menu():
    while True:
        print("GESTOR DE EQUIPOS BIOMÉDICOS")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            print("Finalizando tarea...")
            break
        else:
            print("Opción no válida\n")
if _name_ == "_main_":
    menu()
