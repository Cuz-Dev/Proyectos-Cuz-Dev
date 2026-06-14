#nivel 4

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_5 import Nivel_5
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Nivel_4:
    @staticmethod
    def nivel():
        puntaje = 30
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje,nivel=4,numero=40)
            maquina = random.randint(1,40)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                Nivel_5.nivel()
            elif usuario == 0:
                cf.limpiar_pantalla()
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break
            