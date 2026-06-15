#UI

while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo: ")

class interfaz_terminal:
    @staticmethod
    def menu_principal():
        cf.p("╔══════════════════════════════════════════╗")
        cf.p("          Piedra papel o tijera          ")
        cf.p("╚════════════════════════════════════════════════╝")
        cf.es()
        cf.p("1* Jugar")
        cf.p("2* Puntos")
        cf.p("3* Info")
    @staticmethod
    def juego_nivel(puntaje):
        cf.p(f"Puntaje actual: {puntaje}")
        cf.p("Digita 0 peara guardar puntaje")
        cf.es()
        cf.p("Elige opcion")
        cf.p("[1] piedra")
        cf.p("[2] papel")
        cf.p("[3] tijera")
        cf.es()
    @staticmethod
    def empate(puntaje,maquina):
        print(f"Empate puntaje actual: {puntaje}")
        print(f"Maquina eligio: {maquina}")
    @staticmethod
    def perdiste(puntaje,maquina):
        print(f"Perdiste puntaje actual: {puntaje}")
        print(f"Maquina eligio: {maquina}")
    @staticmethod
    def ganaste(puntaje,maquina):
        print(f"Ganaste puntaje: {puntaje}")
        print(f"Maquina eligio: {maquina}")