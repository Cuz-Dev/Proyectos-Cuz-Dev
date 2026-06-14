#interfaz
while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo necesraio para la ejecucion: ")

class interfaz_de_terminal:
    @staticmethod
    def Menu_principal():
        print("╔══════════════════════════════════════════╗")
        print("             Number hunter               ")
        print("                  V3                       ")
        print("╚══════════════════════════════════════════╝")
        cf.es()
        print('1* Jugar')
        print('2* info, reglas')
        print("3* Puntajes")
        cf.es()
    @staticmethod
    def nivel(puntaje,nivel,numero):
        cf.p(f"➤ Nivel {nivel}  Puntaje actual: {puntaje}")
        cf.p(f"Numero random de 1 al {numero}")
        cf.es()
        cf.p("Digita 0 para guardar puntaje actual: ")
        cf.es()
    