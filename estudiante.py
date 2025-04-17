class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = set()

    def agregar_materia(self, materia):
        self.materias.add(materia)

    def total_materias(self):
        return len(self.materias)
