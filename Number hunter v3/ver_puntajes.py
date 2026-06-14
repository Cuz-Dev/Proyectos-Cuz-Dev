
import os

while True:
    try:
        from configuracion import configuraciones as cf
        break

    except ModuleNotFoundError:
        print("No se encunetra un archivo")

class puntaje:
    @staticmethod
    def ver_Puntaje():
        for archivo in os.listdir("Puntajes"):
            ruta = f"Puntajes/{archivo}"

            with open(ruta, "r") as f:
                puntaje = int(f.read())
            nombre = archivo.replace(".txt", " ")
            print(nombre, puntaje)
            cf.pausa()