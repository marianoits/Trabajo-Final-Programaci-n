from modelos import Estudiante
from gestor_sistema import GestorAsistencia

def cargar_datos_prueba(gestor: GestorAsistencia):
    """Precarga estudiantes, una clase y asistencias para probar rápido."""
    gestor.estudiantes.append(Estudiante(40111222, "Carlos", "Zabaleta", "carlos@mail.com"))
    gestor.estudiantes.append(Estudiante(41222333, "Ana", "Alvarez", "ana@mail.com"))
    gestor.estudiantes.append(Estudiante(42333444, "Luis", "Mendez", "luis@mail.com"))
    
    gestor.habilitar_asistencia(101, "Programación II", "20/11/2026", "18:00", "20:00")
    
    gestor.registrar_asistencia(40111222, 101, "20/11/2026", "18:05")
    gestor.registrar_asistencia(41222333, 101, "20/11/2026", "18:02")
    gestor.registrar_asistencia(42333444, 101, "20/11/2026", "18:10")

def mostrar_menu():
    print("\n" + "="*48)
    print(" SISTEMA DE AUTOGESTIÓN DE ASISTENCIA ")
    print("="*48)
    print("1. [CU 2] Habilitar Asistencia de Clase")
    print("2. [CU 3] Registrar Asistencia")
    print("3. [CU 4] Consultar Asistencias (Ordenadas por Apellido)")
    print("4. [CU 5] Modificar Asistencia")
    print("0. Salir")
    print("="*48)

def main():
    gestor = GestorAsistencia()
    cargar_datos_prueba(gestor)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                print("\n Habilitar Clase ")
                id_clase = int(input("ID de Clase (ej. 102): "))
                materia = input("Nombre de la Materia: ")
                fecha = input("Fecha (DD/MM/AAAA): ")
                inicio = input("Hora inicio (HH:MM): ")
                fin = input("Hora fin (HH:MM): ")
                clase = gestor.habilitar_asistencia(id_clase, materia, fecha, inicio, fin)
                print(f"Clase '{clase.materia.nombre}' (ID: {clase.id_clase}) habilitada.")

            elif opcion == "2":
                print("\n Registrar Asistencia ")
                dni = int(input("DNI del Estudiante (ej. 40111222): "))
                id_clase = int(input("ID de la Clase (ej. 101): "))
                fecha = input("Fecha (DD/MM/AAAA): ")
                hora = input("Hora actual (HH:MM): ")
                asist = gestor.registrar_asistencia(dni, id_clase, fecha, hora)
                print(f"Asistencia registrada (ID: {asist.id_asistencia}): {asist}")

            elif opcion == "3":
                print("\n Listado de Asistencias (Ordenado Alfabéticamente) ")
                lista = gestor.consultar_asistencias()
                if not lista:
                    print("No hay asistencias registradas.")
                else:
                    for a in lista:
                        print(f"ID {a.id_asistencia} - {a}")

            elif opcion == "4":
                print("\n Modificar Asistencia ")
                id_asist = int(input("ID de la Asistencia a modificar (ej. 1, 2 o 3): "))
                nuevo_estado = input("Nuevo estado (ej. Tardanza / Justificado / Ausente): ")
                asist = gestor.modificar_asistencia(id_asist, nuevo_estado)
                print(f"Asistencia actualizada: {asist}")

            elif opcion == "0":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente otra vez.")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()