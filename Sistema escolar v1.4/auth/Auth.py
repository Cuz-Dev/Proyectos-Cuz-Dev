def error_():
    print('No es encuentra el archivo')

while True:
    try:
        from configuracion import limpiar_pantalla, p, es,pedir_tipo_de_usuario, volver,pause
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from configuracion import contraseña_usuario, contraseña_incorrecta, pedir_nueva_contraseña, entrada_us
        break

    except ModuleNotFoundError:
        error_()

while True:
    try:
        from UI import submenu_cambiar_contraseña
        break

    except ModuleNotFoundError:
        error_()

import json
class cambiar_contraseña:
    def Cambiar_contraseña(self):
        with open('auth/logins.json', 'r') as t:
            archivo = json.load(t)
        Usuario = pedir_tipo_de_usuario()
        es()
        contraseña_us = contraseña_usuario()
        es()
        while True:
            try:
                contraseña = archivo['contraseñas'][Usuario]
                break

            except KeyError:
                break
        while True:
            try:
                if contraseña_us == contraseña:
                    limpiar_pantalla()
                    nueva = pedir_nueva_contraseña()
                    archivo['contraseñas'][Usuario] = nueva
                else:
                    limpiar_pantalla()
                    contraseña_incorrecta()
                    pause()
                break


            except UnboundLocalError:
                break

        with open('auth/logins.json', 'w') as r:
            json.dump(archivo, r, indent=4)

        

class sub_menu_cambiar_contraseña:
    def __init__(self):
        self.cambiar = cambiar_contraseña()
    def Sub_Menu_cambio(self):
        while True:
            limpiar_pantalla()
            submenu_cambiar_contraseña()
            opcion = entrada_us()
            es()
            opciones = {
                1: self.cambiar.Cambiar_contraseña
            }
            if opcion in opciones:
                limpiar_pantalla()
                opciones[opcion]()

            else:
                volver()
                limpiar_pantalla()
                break

        
