
def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")

    print("\nDatos Ingresados:")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad}")

if __name__ == "__main__":
    solicitar_datos()
