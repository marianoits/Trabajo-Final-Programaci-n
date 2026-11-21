class Estudiante:
    def __init__(self, dni: int, nombre: str, apellido: str, email: str = ""):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"


class Materia:
    def __init__(self, id_materia: int, nombre: str):
        self.id_materia = id_materia
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_materia})"


class Clase:
    def __init__(self, id_clase: int, materia: Materia, fecha: str, hora_inicio: str, hora_fin: str):
        self.id_clase = id_clase
        self.materia = materia
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.habilitada = False

    def habilitar_registro_asistencia(self):
        self.habilitada = True


class Asistencia:
    def __init__(self, id_asistencia: int, estudiante: Estudiante, clase: Clase, fecha: str, hora: str, estado: str = "Presente"):
        self.id_asistencia = id_asistencia
        self.estudiante = estudiante
        self.clase = clase
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

    def __str__(self):
        return f"[{self.fecha} {self.hora}] {self.clase.materia.nombre} - {self.estudiante.apellido}, {self.estudiante.nombre}: {self.estado}"