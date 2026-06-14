#nivel 2
while True:
    try:
        import random
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        from niveles.nivel_3 import Nivel_3
        break

    except ModuleNotFoundError:
        print("No se encontro el archivo")

class Nivel_2:
    @staticmethod
    def nivel():
        puntaje = 10
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje,nivel=2,numero=20)
            maquina = random.randint(1,20)
            numero_usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if numero_usuario == maquina:
                Nivel_3.nivel()
            elif numero_usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)
                break
            