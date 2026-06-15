# piedra papel o tijera
puntaje = 0
while True:
    try:
        from configuracion import configuraciones as cf
        from UI import interfaz_terminal as i
        from Juego import Nivel_
        from info import ver_info as info
        from puntajes import Puntaje as p
        break
    except ModuleNotFoundError:
        print("No se encontro un archivo: ")

class piedra_papel_o_tijera:
    def __init__(self):
        self.juego = Nivel_()
    def inicio(self):
        while True:
            cf.limpiar_pantalla()
            i.menu_principal()
            opcion = cf.entrada_us()
            opciones = {
                1:self.juego.juego,
                2:p.ver_puntaje,
                3:info.INFO
            }
            if opcion in opciones:
                cf.limpiar_pantalla()
                opciones[opcion]()
            else:
                cf.limpiar_pantalla()
            

iniciar = piedra_papel_o_tijera()
iniciar.inicio()