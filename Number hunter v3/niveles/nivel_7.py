
# nivel 7

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_8 import Nivel_8
        break

    except ModuleNotFoundError:
        print("NO se encontro un archivo")

class Nivel_7:
    @staticmethod
    def nivel():
        puntaje = 60
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje,nivel=7, numero=70)
            maquina = random.randint(1,70)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                Nivel_8.nivel()
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break