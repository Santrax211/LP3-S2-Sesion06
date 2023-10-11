def crear_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f'Se ha creado el archivo "{nombre_archivo}" con éxito.')
    except Exception as e:
        print(f'Error al crear el archivo: {str(e)}')

# Ejemplo de uso
crear_archivo('mi_archivo.txt', 'Este es el contenido del archivo.')


import os

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f'Se ha eliminado el archivo "{nombre_archivo}" con éxito.')
    except Exception as e:
        print(f'Error al eliminar el archivo: {str(e)}')

# Ejemplo de uso
eliminar_archivo('mi_archivo.txt')


def agregar_contenido_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(contenido)
        print(f'Se ha agregado contenido al archivo "{nombre_archivo}" con éxito.')
    except Exception as e:
        print(f'Error al agregar contenido al archivo: {str(e)}')

# Ejemplo de uso
agregar_contenido_archivo('mi_archivo.txt', '\nEste es el nuevo contenido del archivo.')


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except Exception as e:
        print(f'Error al leer el archivo: {str(e)}')
        return None

# Ejemplo de uso
contenido_leido = leer_archivo('mi_archivo.txt')
if contenido_leido is not None:
    print('Contenido del archivo:')
    print(contenido_leido)