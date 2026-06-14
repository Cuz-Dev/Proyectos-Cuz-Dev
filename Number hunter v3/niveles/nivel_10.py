
# nivel 10

while True:
    try:
        import random 
        from configuracion import configuraciones as cf
        from UI import interfaz_de_terminal as i
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo ")

class Nivel_10:
    @staticmethod
    def nivel():
        puntaje = 90
        while True:
            cf.limpiar_pantalla()
            i.nivel(puntaje, nivel=10, numero=100)
            maquina = random.randint(1,100)
            usuario = cf.pedir_numero()
            cf.limpiar_pantalla()
            if usuario == maquina:
                puntaje_final = 100
                cf.game_win(puntaje_final)
                break
            elif usuario == 0:
                cf.guardar_puntaje(puntaje)
            else:
                cf.limpiar_pantalla()
                cf.game_over(maquina)