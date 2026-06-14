
#nivel 6

while True:
    try:
        import random 
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_7 import Nivel_7
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class Nivel_6:
    @staticmethod
    def nivel():
        puntaje = 50
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje,nivel=6,numero=60)
            maquina = random.randint(1, 60)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                Nivel_7.nivel()
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break