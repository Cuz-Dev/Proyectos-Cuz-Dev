import json

with open('auth/logins.json', 'r') as d:
    archivo = json.load(d)

def contraseña_directivo_1():
    contraseña_rector = archivo['contraseñas']['rector']
    return contraseña_rector

def contraseña_directivo_2():
    contraseña_coordinador = archivo['contraseñas']['coordinador']
    return contraseña_coordinador

def contraseña_directivo_3():
    contraseña_docente = archivo['contraseñas']['docente']
    return contraseña_docente
