import os

# Función para mostrar el menú
def menu():
    while True:
        print("Menu")
        print("1. Crear archivo")
        print("2. Eliminar archivo")
        print("3. Agregar contenido")
        print("4. Mostrar contenido de archivo")
        print("5. Listar archivos")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            crear()
        elif opcion == '2':
            eliminar()
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            listar_contenido()
        elif opcion == '5':
            listar_archivos()
        elif opcion == '6':
            salir()
        else:
            error()

# Función para crear un archivo
def crear():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    contenido = input("Ingrese el contenido del archivo: ")

    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f'Se ha creado el archivo "{nombre_archivo}" con éxito.')
    except Exception as e:
        print(f'Error al crear el archivo: {str(e)}')

# Función para eliminar un archivo
def eliminar():
    nombre_archivo = input("Ingrese el nombre del archivo a eliminar: ")
    if os.path.exists(nombre_archivo):
        try:
            os.remove(nombre_archivo)
            print(f'Se ha eliminado el archivo "{nombre_archivo}" con éxito.')
        except Exception as e:
            print(f'Error al eliminar el archivo: {str(e)}')
    else:
        print(f'El archivo "{nombre_archivo}" no ha sido creado.')

# Función para agregar contenido a un archivo
def agregar():
    nombre_archivo = input("Ingrese el nombre del archivo al que desea agregar contenido: ")
    if os.path.exists(nombre_archivo):
        contenido = input("Ingrese el contenido a agregar: ")
        try:
            with open(nombre_archivo, 'a') as archivo:
                archivo.write(contenido)
            print(f'Se ha agregado contenido al archivo "{nombre_archivo}" con éxito.')
        except Exception as e:
            print(f'Error al agregar contenido al archivo: {str(e)}')
    else:
        print(f'El archivo "{nombre_archivo}" no ha sido creado.')

# Función para mostrar el contenido de un archivo
def listar_contenido():
    nombre_archivo = input("Ingrese el nombre del archivo que desea mostrar: ")
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
            print('Contenido del archivo:')
            print(contenido)
        except Exception as e:
            print(f'Error al leer el archivo: {str(e)}')
    else:
        print(f'El archivo "{nombre_archivo}" no ha sido creado.')

# Función para listar los archivos en el directorio actual
def listar_archivos():
    archivos = os.listdir()
    print("Archivos en el directorio actual:")
    for archivo in archivos:
        print(archivo)

# Función para salir del programa
def salir():
    print("Saliendo del programa.")
    exit()

# Función para manejar errores de opción no válida
def error():
    print("Opción no válida. Por favor, elija una opción del menú.")

# Llamada a la función del menú principal
if __name__ == "__main__":
    menu()
