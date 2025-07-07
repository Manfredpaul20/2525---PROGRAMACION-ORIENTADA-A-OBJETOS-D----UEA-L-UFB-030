# programa_poo.py

# Clase base
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo protegido (encapsulación)

    def hacer_sonido(self):
        print("El animal hace un sonido")

    def obtener_nombre(self):
        return self._nombre


# Clase derivada que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Herencia
        self.raza = raza

    # Polimorfismo: Sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self._nombre} dice: ¡Guau!")

    def mostrar_info(self):
        print(f"Perro: {self._nombre}, Raza: {self.raza}")


# Función que demuestra polimorfismo con diferentes objetos
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


if __name__ == "__main__":
    # Crear objetos
    mi_animal = Animal("Animal genérico")
    mi_perro = Perro("Rex", "Labrador")

    # Usar métodos
    print("Ejemplo de encapsulación:")
    print("Nombre del perro:", mi_perro.obtener_nombre())

    print("\nEjemplo de polimorfismo:")
    hacer_sonido_animal(mi_animal)  # Animal genérico
    hacer_sonido_animal(mi_perro)   # Perro con sonido sobrescrito

    print("\nMostrar info del perro:")
    mi_perro.mostrar_info()
