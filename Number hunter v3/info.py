
#info

while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")

class leer:
    @staticmethod
    def leer_info():
        cf.limpiar_pantalla()
        with open("infoh.txt", "r") as f:
            for linea in f:
                print(linea)
        cf.pausa()