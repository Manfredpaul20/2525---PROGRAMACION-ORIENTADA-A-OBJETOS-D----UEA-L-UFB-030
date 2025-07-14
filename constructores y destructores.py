# Clase que representa un recurso que necesita ser gestionado
class Archivo:
    def __init__(self, nombre):
        # Constructor: se llama al crear el objeto
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' ha sido creado y abierto.")

    def escribir(self, contenido):
        # Método para escribir en el archivo
        self.archivo.write(contenido)

    def __del__(self):
        # Destructor: se llama automáticamente cuando el objeto se elimina
        self.archivo.close()
        print(f"Archivo '{self.nombre}' ha sido cerrado y eliminado.")

# Uso de la clase
def main():
    mi_archivo = Archivo("ejemplo.txt")  # Se llama a __init__
    mi_archivo.escribir("Hola, esto es un ejemplo de constructor y destructor en Python.\n")

    # Aquí, cuando el programa termina o eliminamos el objeto, se llama a __del__
    del mi_archivo  # Forzar la eliminación para ver el destructor en acción

if __name__ == "__main__":
    main()
