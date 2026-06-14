#funciones

import os
import random
def abecedario():
    abc = ['a', 'b,' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    return abc

def inicio_():
    persona = str(input('>> Escribe el nombre de el menu:')).lower().strip()
    return persona

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
    p('v2026.1.5')

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
    return int(input('Digite numero de opcion:'))

def Eof():
    p('[ERROR 404] Existe un error con tu compilador:') 

def grado_ejemplo():
    p('Ejemplo "10" ')

def curso_es():
    return str(input('Digite el curso: ')).strip()

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
    p('Guardado con exito ¡! s'\
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
    return str(input('Digite el grado: '))

def curso_es():
    return str(input('Digite el curso: '))


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

def s_n():
    opcion = str(input('seguro que quieres borrar este estudiante s|n :'))
    return opcion

def borrado_exitoso():
    print('Se elimino al estudiante de la base de datos:')

def entrada_usuario():
    return str(input('║ Usuario: ')).lower().strip()

def contraseña_usuario():
    while True:
        try:
            contraseña = int(input('Contraseña: '))
            break

        except ValueError:
            error()
    return contraseña

def pedir_tipo_de_usuario():
    return str(input('Escribe el tipo de directivo: ')).lower().strip()

def contraseña_incorrecta():
    p('contraseña incorrecta')

def contraseña_invalida():
    p('Contraseña invalida:')
    p('Tenga encuenta: ')
    p('1. 6 valores')
    p('2. valores numericos no letras ni simbolos')

def pedir_nueva_contraseña():
    print('Maximo 6 numeros')
    print('no letras')
    while True:
        try:
            nueva = int(input('digite nueva contraseña: '))
            es()
            break

        except ValueError:
            contraseña_invalida()

    while True:
        if len(str(nueva)) == 6:
            break

        else:
            contraseña_incorrecta()
        
    return nueva

def error_clave():
    p('[ERROR] NO se pudo completar accion')
    es()
    p('Posibles causas')
    es()
    p('[1] el curso esta vacio')
    p('y escribiste un apellido,')
    es()
    p('[2] escribiste mal el apellido')

def grado_invalido():
    p('[ERROR] Grado ivalido')
    es()
    p('Grados permitidos')
    es()
    p('6')
    p('7')
    p('8')
    p('9')
    p('10')
    p('11')

def curso_invalido():
    p('[ERROR] Curso ivalido')
    es()
    p('Cursos permitidos')
    es()
    p('1')
    p('2')
    p('3')

def pedir_nombre_guardar():
    return str(input('Escribe el nombre de el estudiante: ')).capitalize().strip()

def pedir_apellido_guardar():
    return str(input('Escribe el apellido: ')).capitalize().strip()

def pedir_grado_guardar():
    return str(input('Dijita el grado: '))

def pedir_curso_guardar():
    return str(input('Dijita el curso: '))

def numero_invalido():
    print('[ERROR] Por favor escribe un numero: ')

def grados_validos():
    grados = [
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
    ]
    return grados

def cursos_validos():
    cursos = [
        '1',
        '2',
        '3',
    ]
    return cursos

def error_nota_estudiante():
    p('[ERROR] No se logro añadir nota')
    es()
    p('Debido a que el estudiante no existe')
    es()
    p(' y pusiste un apellido el cual no existe')
    p('Añade el estudiante primero')

def error_anotacion_estudiante():
    p('[ERROR] No se logro añadir anotaciones')
    es()
    p('Debido a que el estudiante no existe')
    es()
    p(' y pusiste un apellido el cual no existe')
    p('Añade el estudiante primero')
    es()
    p('O verifica si escribiste bien el apellido')

def error_boletin_estudiante():
    p('[ERROR] No se logro añadir boletin')
    p('Debido a que el estudiante no existe')
    es()
    p(' o pusiste un apellido el cual no existe')
    p('Añade el estudiante primero')
    es()
    p('O verifica si escribiste bien el apellido')
    

def pedir_nombre_acudiente():
    return str(input('Escribe el nombre de el acudiente: ')).lower().strip()

def pedir_periodo():
    while True:
        try:
            periodo = int(input("Digita periodo actual para boletin: "))
            break
        except ValueError:
            error()
    return periodo

def pedir_numero_boletin():
    while True:
        try:
            numero = int(input("Digita numero de boletin: "))
            break

        except ValueError:
            error()
    return numero

def pedir_apellido_boletin():
    return str(input("Escribe el apellido de el estudiante: ")).capitalize()


