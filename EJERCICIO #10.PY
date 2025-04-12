# Programa que suma números hasta que el usuario ingrese 0

suma_total = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    
    if numero == 0:
        break  
    
    suma_total += numero  

print("La suma total es:", suma_total)
