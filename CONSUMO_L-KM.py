print ("Ricardo Martínez Estrada")
print (" ")

# Código donde se le solicite la información al usuario.
kilometros = float(input("Ingrese los kilometros recorridos por su moto: "))
combustible = float(input("Ingrese la cantidad de litros consumidos durante el viaje: "))


# Dividir los valores para obtener el consumo de combustible por kilometro.
division = (combustible/kilometros)
print ("El consumo de combustible (litro) por kilometro es: ", division)