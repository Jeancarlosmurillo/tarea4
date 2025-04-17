from gestor_inscripciones import GestorInscripciones

if __name__ == "__main__":
    ruta = "C:\\Users\\JEAN CARLOS\\Desktop\\2025_1\\ingenieriaSoftware1\\tarea4\\tarea4.csv"
    gestor = GestorInscripciones()
    gestor.cargar_csv(ruta)
    gestor.mostrar_resultado()
