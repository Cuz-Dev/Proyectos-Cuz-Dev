
#nivel 5

while True:
    try:
        import random
        from  configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_6 import Nivel_6
        break
    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Nivel_5:
    @staticmethod
    def nivel():
        puntaje = 40
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje, nivel=5, numero=50)
            maquina = random.randint(1,50)
            usuario = cf.pedir_numero()
            if usuario == maquina:
                Nivel_6.nivel()
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break
