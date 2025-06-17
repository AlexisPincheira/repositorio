suma = 0
numero = int(input("Ingresa un número positivo (ingresa un número negativo para salir): "))

while numero >= 0:
    suma += numero
    numero = int(input("Ingresa otro número positivo (o un número negativo para salir): "))

print("La suma de los números ingresados es:", suma)
