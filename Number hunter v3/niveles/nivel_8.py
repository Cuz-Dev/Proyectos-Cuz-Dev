
#nivel 8

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_9 import Nivel_9
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Nivel_8:
    @staticmethod
    def nivel():
        puntaje = 70
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje, nivel=8, numero=80)
            maquina = random.randint(1,80)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                Nivel_9.nivel()
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break