print("Martínez Estrada Ricardo")
print("Programa que adivina un número del 1 al 10")
print(" ")

# Almacenar un número secreto
numero_secreto = 7  # Puedes cambiar este número

# Solicitar al usuario que adivine el número
adivinanza = input("Adivina el número entre 1 y 10: ")
num_adivinanza = int(adivinanza)

# Verificar si la adivinanza es correcta
if num_adivinanza == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Lo siento, intenta de nuevo.")
