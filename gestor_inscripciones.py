import csv
from estudiante import Estudiante

class GestorInscripciones:
    def __init__(self):
        self.estudiantes = {}

    def cargar_csv(self, ruta_archivo):
        try:
            with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    if len(fila) != 4:
                        print("Línea inválida:", fila)
                        continue
                    cedula, nombre, cod_materia, nom_materia = fila
                    if cedula not in self.estudiantes:
                        self.estudiantes[cedula] = Estudiante(cedula, nombre)
                    self.estudiantes[cedula].agregar_materia(nom_materia)
        except FileNotFoundError:
            print("❌ El archivo no fue encontrado. Verifica la ruta.")

    def mostrar_resultado(self):
        for estudiante in self.estudiantes.values():
            print(f"{estudiante.nombre}: {estudiante.total_materias()} materias")
