from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from utils import leer_entero
from utils import mostrar_opciones, menu
from utils import borrar_pantalla

pila = MiPila(10)
cola = MiCola(10)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        borrar_pantalla()
        mostrar_opciones("Menú Pila", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            borrar_pantalla()
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero is None:
                print("  ⚠ La pila está vacía")
            else:
                print(f"  ✓ Desapilado: {pasajero}")
        elif op == "4":
            pasajero = pila.ver_tope()
            if pasajero is None:
                print("  ⚠ La pila está vacía")
            else:
                print(f"  Tope: {pasajero}")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero: ")
            if pila.eliminar_por_numero(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = pila.copiar()
            print("  ✓ Copia de la pila:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  La pila está vacía")
            else:
                print("  La pila no está vacía")
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba cargados (sin repetir números)")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        borrar_pantalla()
        mostrar_opciones("Menú Cola", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            borrar_pantalla()
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero is None:
                print("  ⚠ La cola está vacía")
            else:
                print(f"  ✓ Desencolado: {pasajero}")
        elif op == "4":
            pasajero = cola.ver_frente()
            if pasajero is None:
                print("  ⚠ La cola está vacía")
            else:
                print(f"  Frente: {pasajero}")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion].nombre}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero: ")
            if cola.eliminar_por_numero(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = cola.copiar()
            print("  ✓ Copia de la cola:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  La cola no está vacía")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba cargados (sin repetir números)")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        borrar_pantalla()
        op = menu("Menú Principal", ["1) Pila", "2) Cola", "0) Salir"])

        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "0":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
