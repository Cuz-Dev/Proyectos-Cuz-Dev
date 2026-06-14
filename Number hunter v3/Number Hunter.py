#number hunter v3
#desarrollador cuz-dev

while True:
    try:
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as inf
        from niveles import Nivel_1
        from info import leer
        from ver_puntajes import puntaje
        break
    except ModuleNotFoundError:
        print("No se encontro un archivo")

class  Number_hunter:
    def Menu_principal(self):
        while True:
            cf.limpiar_pantalla()
            inf.Menu_principal()
            opcion = cf.entrada_us()
            opciones = {
                1:Nivel_1.Nivel,
                2:leer.leer_info,
                3:puntaje.ver_Puntaje
            }
            if opcion in opciones:
                cf.limpiar_pantalla()
                opciones[opcion]()
            else:
                cf.limpiar_pantalla()

iniciar = Number_hunter()
iniciar.Menu_principal()

