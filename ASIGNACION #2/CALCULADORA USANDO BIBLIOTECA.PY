import math

print("Calculadora usando la biblioteca 'math'")

numero = float(input("Ingresa un número: "))

print("Raíz cuadrada:", math.sqrt(numero))
print("Seno:", math.sin(math.radians(numero)))
print("Coseno:", math.cos(math.radians(numero)))
print("Potencia (número al cuadrado):", math.pow(numero, 2))
