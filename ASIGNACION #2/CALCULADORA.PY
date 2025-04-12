def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"

# Menú básico
print("Calculadora con funciones")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Elige operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", sumar(num1, num2))
elif operacion == "-":
    print("Resultado:", restar(num1, num2))
elif operacion == "*":
    print("Resultado:", multiplicar(num1, num2))
elif operacion == "/":
    print("Resultado:", dividir(num1, num2))
else:
    print("Operación no válida")
