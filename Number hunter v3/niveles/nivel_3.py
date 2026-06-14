#nivel 3

while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_4 import Nivel_4
        break

    except ModuleNotFoundError:
        print("No se encuentra un archivo:")

class Nivel_3:
    @staticmethod
    def nivel():
        puntaje = 20
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje,nivel=3,numero=30)
            maquina = random.randint(1,30)
            numero_usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if numero_usuario == maquina:
                Nivel_4.nivel()
            elif numero_usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break
