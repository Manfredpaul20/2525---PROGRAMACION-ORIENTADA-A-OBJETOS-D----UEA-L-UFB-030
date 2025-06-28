# Programa para calcular el área de un triángulo
# Usa variables con tipos de datos: float, int, string, boolean

def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo usando la fórmula (base * altura) / 2
    """
    return (base * altura) / 2

# Entrada de datos
nombre_usuario = input("Ingresa tu nombre: ")  # string
print(f"Hola, {nombre_usuario}. Vamos a calcular el área de un triángulo.")

base = float(input("Ingresa la base del triángulo en cm: "))  # float
altura = float(input("Ingresa la altura del triángulo en cm: "))  # float

# Cálculo
area = calcular_area_triangulo(base, altura)

# Resultado
print(f"El área del triángulo es {area} cm²")  # float
area_valida = area > 0  # boolean
print(f"¿El área calculada es válida? {area_valida}")
