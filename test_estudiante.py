import unittest
from estudiante import Estudiante

class TestEstudiante(unittest.TestCase):
    
    def test_agregar_materia_nueva(self):
        estudiante = Estudiante(123, "Lulú López")
        estudiante.agregar_materia("Cálculo")
        self.assertIn("Cálculo", estudiante.materias)
        self.assertEqual(len(estudiante.materias), 1)

    def test_agregar_materia_duplicada(self):
        estudiante = Estudiante(123, "Lulú López")
        estudiante.agregar_materia("Cálculo")
        estudiante.agregar_materia("Cálculo")  # Intento duplicado
        self.assertEqual(estudiante.materias.count("Cálculo"), 1)
        self.assertEqual(len(estudiante.materias), 1)

if __name__ == '__main__':
    unittest.main()
