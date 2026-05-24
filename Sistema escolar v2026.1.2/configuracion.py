#funciones

import os
import random
def abecedario():
    abc = ['a', 'b,' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    return abc

def simbolos():
        simbolos = (
            '#',
            '!',
            '@',
            '$',
            '%',
            '&',
            '¿',
            '?',
            '.',
            ',',
            ':',
            '*'
        )

        return simbolos

def numero_random():
    return str(random.randint(0,9))

def curso_ejemplo():
    p('Ejemplo "1" ')

def es():
    print('  ')

def pause():
    es()
    input('Presiona enter para salir <')
    es()

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")

def letra_random():
        return str(random.choice(abecedario()))

def simbolo_random():
    return str(random.choice(simbolos()))

def p(mensaje):
    print(mensaje)

def v():
    es()
    p('v2026.1.2')

def error():
    es()
    p('[ERROR 505] Debes escribir un numero no una letra')
    es()

def volver():
    p('<<<<')
    es()

def salir():
    p('Saliendo*.*')
    es()

def entrada_us():
    return int(input('dijita numero de opcion:'))

def Eof():
    p('[ERROR 404] Existe un error con tu compilador:') 

def grado_ejemplo():
    p('Ejemplo "10" ')

def curso_es():
    return str(input('Dijita el curso: ')).strip()

def curso_inesistente():
    p('[ERROR] Ese curso no existe: ')

def grado_inesistente():
    p('[ERROR] Ese grado no existe: ')

def generando():
    es()
    p('Generando □ ■ ▫ ▪')

def guardando():
    es()
    p('Guardando □ ■ ▫ ▪')
    es()

def guardado_exito():
    es()
    p('Guardado con exito ¡! s' \
    'sEn save password.txt')
    es()

def finalized():
    p('Contraseña finalizada Con exito: ')

def linea_menu():
    p('────────────────────────────────────────────────')

def linea_menu2():
    p('------------------------------------------------')

def linea_submenu():
    p('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def mostrar_generar():
    es()
    p('[1] Empezar a generar 🔥')
    p('[2] <<<< Volver')
    es()

def error_es():
    p('[ERROR 101] No se encuentra el archivo save password.txt')
    p('!¡Sin ese archivo no se puede guardar las contraseñas que crees¡!')

def salir_s():
    return str(input('Escribe s para salir:')).lower()

def error_usuario():
    es()
    p('[ERROR] Nombre de usuario invalido: ')
    es()

def grado_es():
    return str(input('Dijita el grado: '))

def curso_es():
    return str(input('Dijita el curso: '))


def entrada():
    while True:
        try:
            opcion = int(input('dijita numero de opcion:'))
            es()
            break

        except ValueError:
            limpiar_pantalla()
            error()

    return opcion

def salir_menu_info():
    while True:
        try:
            sa = int(input('Escribe 1* para salir:'))
            while sa != 1:
                sa = int(input('!¡Escribe 1 para salir¡!:'))
            break

        except ValueError:
            error()

def mostrar_info():
    while True:
        try:
            es()
            with open("info.txt", "r") as archivo:
                for linea in archivo:
                    p(linea.strip())
            break
        except ModuleNotFoundError:
            p('NO se encuentra el archivo info.txt')

def anotacion_():
    lineas = []

    p('Escribe la anotacion')
    p('Para finalizar anotacion escribe Fn')
    es()
    p('Anotacion: ')

    while True:
        texto = input()

        if texto == 'Fn':
            break

        lineas.append(texto)

    anotacion = "\n".join(lineas)
    return anotacion
