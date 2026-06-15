#info

while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encontro un archivo")


class ver_info:
    @staticmethod
    def INFO():
        cf.limpiar_pantalla()
        with open("info.txt", "r") as f:
            for linea in f:
                print(linea)
        cf.pausa()