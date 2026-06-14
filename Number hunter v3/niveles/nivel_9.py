
#nivel 9

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from  niveles.nivel_10 import Nivel_10
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Nivel_9:
    @staticmethod
    def nivel():
        puntaje = 80
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje, nivel=9, numero=90)
            maquina = random.randint(1,80)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                Nivel_10.nivel()
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break