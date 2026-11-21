from modelos import Estudiante, Materia, Clase, Asistencia

class GestorAsistencia:
    def __init__(self):
        self.estudiantes = []
        self.clases = []
        self.asistencias = []

    # CU N° 2: Habilitar Asistencia
    def habilitar_asistencia(self, id_clase: int, nombre_materia: str, fecha: str, hora_inicio: str, hora_fin: str) -> Clase:
        materia = Materia(id_clase, nombre_materia)
        nueva_clase = Clase(id_clase, materia, fecha, hora_inicio, hora_fin)
        nueva_clase.habilitar_registro_asistencia()
        self.clases.append(nueva_clase)
        return nueva_clase

    # CU N° 3: Registrar Asistencia
    def registrar_asistencia(self, dni_estudiante: int, id_clase: int, fecha: str, hora: str) -> Asistencia:
        estudiante_encontrado = None
        for e in self.estudiantes:
            if e.dni == dni_estudiante:
                estudiante_encontrado = e
                break

        if estudiante_encontrado is None:
            raise ValueError("Estudiante no encontrado.")

        clase_encontrada = None
        for c in self.clases:
            if c.id_clase == id_clase:
                clase_encontrada = c
                break

        if clase_encontrada is None or not clase_encontrada.habilitada:
            raise ValueError("Clase no encontrada o no habilitada.")

        nueva_asistencia = Asistencia(len(self.asistencias) + 1, estudiante_encontrado, clase_encontrada, fecha, hora)
        self.asistencias.append(nueva_asistencia)
        return nueva_asistencia

    # Algoritmo de Ordenamiento: QuickSort por apellido
    def _quicksort(self, lista: list) -> list:
        if len(lista) <= 1:
            return lista
        
        pivote = lista[0]
        pivote_apellido = pivote.estudiante.apellido.lower()
        
        menores = []
        mayores = []
        for x in lista[1:]:
            if x.estudiante.apellido.lower() <= pivote_apellido:
                menores.append(x)
            else:
                mayores.append(x)
        
        return self._quicksort(menores) + [pivote] + self._quicksort(mayores)

    def ordenar_asistencias_por_apellido(self) -> list:
        return self._quicksort(self.asistencias.copy())

    # CU N° 4: Consultar Asistencias
    def consultar_asistencias(self) -> list:
        return self.ordenar_asistencias_por_apellido()

    # CU N° 5: Modificar Asistencia
    def modificar_asistencia(self, id_asistencia: int, nuevo_estado: str) -> Asistencia:
        for asistencia in self.asistencias:
            if asistencia.id_asistencia == id_asistencia:
                asistencia.estado = nuevo_estado
                return asistencia

        raise ValueError(f"No se encontró la asistencia con ID {id_asistencia}.")