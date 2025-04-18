class Estudiante:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)

    def total_materias(self):
        return len(self.materias)
