import unittest
from modelos import Estudiante, Materia, Clase, Asistencia
from gestor_sistema import GestorAsistencia

class TestSistemaAsistencia(unittest.TestCase):

    #  4 TESTS DE CLASES 
    def test_clase_estudiante(self):
        e = Estudiante(40111222, "Juan", "Perez", "juan@mail.com")
        self.assertEqual(e.dni, 40111222)
        self.assertEqual(e.apellido, "Perez")

    def test_clase_materia(self):
        m = Materia(1, "Programación II")
        self.assertEqual(m.nombre, "Programación II")

    def test_clase_clase(self):
        m = Materia(1, "Base de Datos")
        c = Clase(10, m, "2026-11-20", "18:00", "20:00")
        self.assertFalse(c.habilitada)
        c.habilitar_registro_asistencia()
        self.assertTrue(c.habilitada)

    def test_clase_asistencia(self):
        e = Estudiante(111, "Lucas", "Sosa")
        c = Clase(1, Materia(1, "Inglés"), "2026-11-20", "18:00", "19:00")
        a = Asistencia(1, e, c, "2026-11-20", "18:05")
        self.assertEqual(a.estado, "Presente")

    #  4 TESTS DE CASOS DE USO 
    def test_cu2_habilitar_asistencia(self):
        gestor = GestorAsistencia()
        clase = gestor.habilitar_asistencia(50, "Matemática", "2026-11-20", "19:00", "21:00")
        self.assertTrue(clase.habilitada)

    def test_cu3_registrar_asistencia(self):
        gestor = GestorAsistencia()
        gestor.estudiantes.append(Estudiante(99888777, "Pedro", "Acosta"))
        gestor.habilitar_asistencia(10, "Sistemas", "2026-11-20", "18:00", "20:00")
        asistencia = gestor.registrar_asistencia(99888777, 10, "2026-11-20", "18:10")
        self.assertEqual(asistencia.estudiante.nombre, "Pedro")

    def test_cu4_consultar_asistencias_ordenadas(self):
        gestor = GestorAsistencia()
        gestor.estudiantes.append(Estudiante(1, "Carlos", "Zapata"))
        gestor.estudiantes.append(Estudiante(2, "Ana", "Alonso"))
        gestor.habilitar_asistencia(10, "Redes", "2026-11-20", "18:00", "20:00")
        
        gestor.registrar_asistencia(1, 10, "2026-11-20", "18:00")
        gestor.registrar_asistencia(2, 10, "2026-11-20", "18:05")
        
        resultado = gestor.consultar_asistencias()
        self.assertEqual(resultado[0].estudiante.apellido, "Alonso")
        self.assertEqual(resultado[1].estudiante.apellido, "Zapata")

    def test_cu5_modificar_asistencia(self):
        gestor = GestorAsistencia()
        gestor.estudiantes.append(Estudiante(1, "Carlos", "Zapata"))
        gestor.habilitar_asistencia(10, "Redes", "2026-11-20", "18:00", "20:00")
        asist = gestor.registrar_asistencia(1, 10, "2026-11-20", "18:00")
        
        actualizada = gestor.modificar_asistencia(asist.id_asistencia, "Tardanza")
        self.assertEqual(actualizada.estado, "Tardanza")

if __name__ == "__main__":
    unittest.main()